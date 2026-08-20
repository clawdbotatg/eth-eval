// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Answer} from "../../src/Answer.sol";

interface INPMView {
    function balanceOf(address) external view returns (uint256);
    function tokenOfOwnerByIndex(address, uint256) external view returns (uint256);
    /// returned as a struct, not a 12-tuple - destructuring it is stack-too-deep
    struct Pos {
        uint96 nonce; address operator; address token0; address token1; uint24 fee;
        int24 tickLower; int24 tickUpper; uint128 liquidity;
        uint256 f0; uint256 f1; uint128 owed0; uint128 owed1;
    }
    function positions(uint256) external view returns (Pos memory);
}

/// Minting a real v3 position: the struct has 11 fields, token order is fixed
/// by address, ticks must be spacing-aligned, and the amounts have to match
/// the range's ratio or most of the purse is handed straight back.
contract Grader is Test {
    address constant USER = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
    uint256 constant WETH_IN = 10 ether;
    uint256 constant USDC_IN = 20_000e6;
    uint256 constant PX = 1900e6;          // USDC per WETH, to value leftovers
    int24   constant CUR = 200808;

    function test_grade() public {
        deal(Mainnet.WETH, USER, WETH_IN);
        deal(Mainnet.USDC, USER, USDC_IN);
        vm.startPrank(USER);
        IERC20(Mainnet.WETH).approve(Mainnet.NPM, type(uint256).max);
        IERC20(Mainnet.USDC).approve(Mainnet.NPM, type(uint256).max);
        (bool ok, ) = Mainnet.NPM.call(Answer.CALLDATA);
        assertTrue(ok, "mint calldata reverted on the position manager");
        vm.stopPrank();

        assertEq(INPMView(Mainnet.NPM).balanceOf(USER), 1, "no position NFT minted to the recipient");
        uint256 id = INPMView(Mainnet.NPM).tokenOfOwnerByIndex(USER, 0);
        INPMView.Pos memory p = INPMView(Mainnet.NPM).positions(id);

        assertEq(p.token0, Mainnet.USDC, "token0 must be USDC (lower address)");
        assertEq(p.token1, Mainnet.WETH, "token1 must be WETH");
        assertEq(uint256(p.fee), 3000, "wrong fee tier");
        assertEq(int256(p.tickLower) % 60, 0, "tickLower not aligned to tickSpacing 60");
        assertEq(int256(p.tickUpper) % 60, 0, "tickUpper not aligned to tickSpacing 60");
        assertTrue(p.tickLower <= CUR && CUR < p.tickUpper, "range does not bracket the current tick");
        assertGe(int256(CUR) - int256(p.tickLower), 100, "lower side under 1%");
        assertGe(int256(p.tickUpper) - int256(CUR), 100, "upper side under 1%");
        assertLe(int256(CUR) - int256(p.tickLower), 149, "lower side over 1.5%");
        assertLe(int256(p.tickUpper) - int256(CUR), 149, "upper side over 1.5%");

        // capital actually deployed, valued in USDC
        uint256 left = IERC20(Mainnet.USDC).balanceOf(USER)
                     + (IERC20(Mainnet.WETH).balanceOf(USER) * PX) / 1e18;
        uint256 offered = USDC_IN + (WETH_IN * PX) / 1e18;
        assertLe(left * 100 / offered, 10, "over 10% of the purse was refunded - amounts do not match the range");

        // tight + balanced is the whole point: a wide range deploys the same
        // capital at a fifth of the liquidity
        assertGe(uint256(p.liquidity), 6.5e16, "liquidity too low for the capital - range not tight or amounts unbalanced");
    }
}
