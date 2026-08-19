// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Vault} from "../../src/Submission.sol";

contract Grader is Test {
    Vault v;
    address usdc = Mainnet.USDC;
    address alice = address(0xA11CE);
    address bob   = address(0xB0B);

    function setUp() public {
        v = new Vault(usdc);
        for (uint256 i = 0; i < 2; i++) {
            address u = i == 0 ? alice : bob;
            deal(usdc, u, 5_000_000e6);
            vm.prank(u); IERC20(usdc).approve(address(v), type(uint256).max);
        }
    }
    function _dep(address u, uint256 a) internal returns (uint256 s) { vm.prank(u); s = v.deposit(a); }
    function _red(address u, uint256 s) internal returns (uint256 a) { vm.prank(u); a = v.redeem(s); }

    /// YIELD: a direct transfer must accrue to existing holders, not vanish.
    function testFuzz_yield_accrues_to_holders(uint96 x, uint96 y) public {
        uint256 dep   = bound(uint256(x), 1_000e6, 1_000_000e6);
        uint256 yield = bound(uint256(y), 100e6, 500_000e6);
        uint256 s = _dep(alice, dep);
        deal(usdc, address(this), yield);
        IERC20(usdc).transfer(address(v), yield);          // yield arrives
        uint256 out = _red(alice, s);
        assertGt(out, dep, "yield did not reach the only depositor");
        assertLe(out, dep + yield, "paid out more than deposit + yield");
    }

    /// FAIRNESS: someone who arrives AFTER the yield must not take a cut of it.
    /// This is what separates real share accounting from minting 1:1.
    function testFuzz_late_depositor_does_not_dilute(uint96 x, uint96 y) public {
        uint256 a     = bound(uint256(x), 10_000e6, 1_000_000e6);
        uint256 yield = bound(uint256(y), 1_000e6, 500_000e6);

        uint256 sa = _dep(alice, a);
        deal(usdc, address(this), yield);
        IERC20(usdc).transfer(address(v), yield);   // alice owns 100% here

        uint256 sb = _dep(bob, a);                  // bob arrives late, same size
        uint256 outB = _red(bob, sb);
        uint256 outA = _red(alice, sa);

        assertLe(outB, a + (yield / 100), "late depositor captured the earlier holder's yield");
        assertGe(outA, a + (yield * 99) / 100, "early holder was diluted by a late depositor");
    }

    /// NO FREE MONEY: an immediate round trip never profits.
    function testFuzz_round_trip_never_profits(uint96 x, uint96 y) public {
        uint256 a = bound(uint256(x), 1e6, 1_000_000e6);
        uint256 b = bound(uint256(y), 1e6, 1_000_000e6);
        _dep(bob, b);
        uint256 before = IERC20(usdc).balanceOf(alice);
        uint256 sa = _dep(alice, a);
        _red(alice, sa);
        assertLe(IERC20(usdc).balanceOf(alice), before, "round trip printed money");
    }

    /// SOLVENCY: everyone exiting must never overdraw the vault.
    function testFuzz_solvent_on_exit(uint96 x, uint96 y) public {
        uint256 a = bound(uint256(x), 1e6, 1_000_000e6);
        uint256 b = bound(uint256(y), 1e6, 1_000_000e6);
        uint256 sa = _dep(alice, a);
        uint256 sb = _dep(bob, b);
        // the task spec never promised a totalShares() getter - grade only what
        // it asked for: both holders can exit, and the vault is not overdrawn.
        uint256 outA = _red(alice, sa);
        uint256 outB = _red(bob, sb);
        assertLe(outA + outB, a + b, "paid out more than was ever deposited");
    }

    /// INFLATION ATTACK: dust deposit + donation must not steal the next depositor.
    function test_inflation_attack_fails() public {
        uint256 sa;
        uint256[4] memory tries = [uint256(1), 1e3, 1e6, 1e8];
        for (uint256 i = 0; i < tries.length; i++) {
            vm.prank(alice);
            try v.deposit(tries[i]) returns (uint256 s) { sa = s; break; } catch {}
        }
        assertGt(sa, 0, "vault rejected every attacker deposit size");
        vm.prank(alice); IERC20(usdc).transfer(address(v), 100_000e6);

        uint256 sb = _dep(bob, 100_000e6);
        assertGt(sb, 0, "victim minted zero shares");
        uint256 out = _red(bob, sb);
        assertGe(out, 99_000e6, "victim lost more than 1% to the attacker");
    }

    /// Still usable: a lone depositor gets essentially all of it back.
    function test_round_trip_is_fair() public {
        uint256 s = _dep(alice, 100_000e6);
        assertGe(_red(alice, s), 99_990e6, "lone depositor lost more than 0.01%");
    }
}
