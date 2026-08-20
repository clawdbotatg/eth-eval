// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Rebalancer} from "../../src/Submission.sol";

interface INPMView {
    function balanceOf(address) external view returns (uint256);
    function tokenOfOwnerByIndex(address, uint256) external view returns (uint256);
    struct Pos {
        uint96 nonce; address operator; address token0; address token1; uint24 fee;
        int24 tickLower; int24 tickUpper; uint128 liquidity;
        uint256 f0; uint256 f1; uint128 owed0; uint128 owed1;
    }
    function positions(uint256) external view returns (Pos memory);
}

/// A WETH-heavy purse CANNOT fill a tight symmetric range - at this block a
/// 50 WETH + 5000 USDC purse tops out near 49% deployed however far the lower
/// tick is pushed. The only way to hit 90% is to swap into the right ratio
/// first and then mint. That is the whole task.
contract Grader is Test {
    Rebalancer r;
    uint256 constant WETH_IN = 50 ether;
    uint256 constant USDC_IN = 5_000e6;
    uint256 constant PX = 1900e6;      // USDC per WETH, for valuation
    int24   constant CUR = 200808;

    function _value(address who) internal view returns (uint256) {
        return IERC20(Mainnet.USDC).balanceOf(who)
             + (IERC20(Mainnet.WETH).balanceOf(who) * PX) / 1e18;
    }

    function test_grade() public {
        r = new Rebalancer();
        deal(Mainnet.WETH, address(r), WETH_IN);
        deal(Mainnet.USDC, address(r), USDC_IN);
        uint256 offered = USDC_IN + (WETH_IN * PX) / 1e18;

        r.provide();

        assertEq(INPMView(Mainnet.NPM).balanceOf(address(r)), 1, "no position NFT held by the contract");
        uint256 id = INPMView(Mainnet.NPM).tokenOfOwnerByIndex(address(r), 0);
        INPMView.Pos memory p = INPMView(Mainnet.NPM).positions(id);

        assertEq(p.token0, Mainnet.USDC, "token0 must be USDC");
        assertEq(p.token1, Mainnet.WETH, "token1 must be WETH");
        assertEq(uint256(p.fee), 3000, "must use the 0.30% pool");
        assertEq(int256(p.tickLower) % 60, 0, "tickLower not aligned to spacing 60");
        assertEq(int256(p.tickUpper) % 60, 0, "tickUpper not aligned to spacing 60");
        assertTrue(p.tickLower <= CUR && CUR < p.tickUpper, "range does not bracket the current tick");
        assertGe(int256(CUR) - int256(p.tickLower), 100, "lower side under 1%");
        assertGe(int256(p.tickUpper) - int256(CUR), 100, "upper side under 1%");
        assertLe(int256(CUR) - int256(p.tickLower), 248, "lower side over 2.5%");
        assertLe(int256(p.tickUpper) - int256(CUR), 248, "upper side over 2.5%");
        assertGt(uint256(p.liquidity), 0, "position has no liquidity");

        // whatever is left sitting in the contract is capital that was not deployed
        uint256 left = _value(address(r));
        assertLe(left * 100 / offered, 10, "under 90% of the purse was deployed - it was not rebalanced");
    }
}
