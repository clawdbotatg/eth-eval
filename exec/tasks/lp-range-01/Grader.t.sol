// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IUniV3Pool, IV3Factory} from "../../src/Common.sol";
import {Answer} from "../../src/Answer.sol";

/// WETH/USDC 0.30% pool. A valid tight range must be tick-spacing aligned,
/// must bracket the live tick, and must cover >=1% but <=2.5% each side.
contract Grader is Test {
    function test_grade() public view {
        address pool = IV3Factory(Mainnet.V3_FACTORY).getPool(Mainnet.WETH, Mainnet.USDC, 3000);
        (, int24 cur, , , , , ) = IUniV3Pool(pool).slot0();
        int24 spacing = IUniV3Pool(pool).tickSpacing();

        int24 lo = Answer.TICK_LOWER;
        int24 hi = Answer.TICK_UPPER;

        assertTrue(lo < hi, "tickLower must be below tickUpper");
        assertEq(int256(lo) % int256(spacing), 0, "tickLower not aligned to tickSpacing");
        assertEq(int256(hi) % int256(spacing), 0, "tickUpper not aligned to tickSpacing");
        assertTrue(lo <= cur && cur < hi, "range does not contain the current tick");

        // 1.0001^100 ~= +1.005% ; 1.0001^248 ~= +2.51%
        assertGe(int256(cur) - int256(lo), 100, "lower side narrower than 1%");
        assertGe(int256(hi) - int256(cur), 100, "upper side narrower than 1%");
        assertLe(int256(cur) - int256(lo), 248, "lower side wider than 2.5%");
        assertLe(int256(hi) - int256(cur), 248, "upper side wider than 2.5%");
    }
}
