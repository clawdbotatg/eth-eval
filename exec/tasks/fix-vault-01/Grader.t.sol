// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Vault} from "../../src/Submission.sol";

/// The fix must kill the donation/first-depositor share-inflation attack
/// WITHOUT breaking ordinary deposits and withdrawals.
contract Grader is Test {
    Vault v;
    address attacker = address(0xA11CE);
    address victim   = address(0xB0B);
    address usdc     = Mainnet.USDC;

    function setUp() public {
        v = new Vault(usdc);
        deal(usdc, attacker, 100_000e6);
        deal(usdc, victim,   100_000e6);
        vm.prank(attacker); IERC20(usdc).approve(address(v), type(uint256).max);
        vm.prank(victim);   IERC20(usdc).approve(address(v), type(uint256).max);
    }

    /// Seed the attacker's position with the SMALLEST deposit the vault accepts.
    /// Rejecting dust is itself a legitimate mitigation, so a revert here must
    /// not be scored as a failed fix - we escalate instead of giving up.
    function _attackerSeed() internal returns (bool seeded) {
        uint256[5] memory tries = [uint256(1), 1e3, 1e6, 1e8, 1e9];
        for (uint256 i = 0; i < tries.length; i++) {
            vm.prank(attacker);
            try v.deposit(tries[i]) returns (uint256) { return true; } catch {}
        }
        return false;
    }

    /// EXPLOIT: a tiny deposit then a direct donation must not steal the victim's deposit.
    function test_inflation_attack_fails() public {
        assertTrue(_attackerSeed(), "vault rejected every deposit size");
        vm.prank(attacker); IERC20(usdc).transfer(address(v), 10_000e6); // donation

        uint256 before = IERC20(usdc).balanceOf(victim);
        vm.prank(victim); uint256 s = v.deposit(10_000e6);
        assertGt(s, 0, "victim minted zero shares - inflation attack still works");

        vm.prank(victim); v.withdraw(s);
        uint256 recovered = IERC20(usdc).balanceOf(victim) - (before - 10_000e6);
        assertGe(recovered, 9_900e6, "victim lost more than 1% to the attacker");
    }

    /// FEATURE: a lone depositor gets all of it back.
    function test_round_trip() public {
        vm.prank(victim); uint256 s = v.deposit(1_000e6);
        assertGt(s, 0, "no shares minted");
        uint256 before = IERC20(usdc).balanceOf(victim);
        vm.prank(victim); v.withdraw(s);
        assertGe(IERC20(usdc).balanceOf(victim) - before, 999e6, "round trip lost funds");
    }

    /// FEATURE: equal deposits get equal claims.
    function test_two_depositors_share_fairly() public {
        vm.prank(attacker); uint256 sa = v.deposit(5_000e6);
        vm.prank(victim);   uint256 sv = v.deposit(5_000e6);
        assertApproxEqRel(sa, sv, 0.01e18, "equal deposits did not get equal shares");
    }
}
