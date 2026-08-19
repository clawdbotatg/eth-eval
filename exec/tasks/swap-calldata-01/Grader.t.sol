// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Answer} from "../../src/Answer.sol";

contract Grader is Test {
    address constant USER = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
    /// the WETH/USDC 0.05% pool — checking its balance is what proves the
    /// right fee tier was used; output size alone cannot tell the tiers apart.
    address constant POOL_500 = 0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640;

    function test_grade() public {
        deal(Mainnet.WETH, USER, 5 ether);
        vm.startPrank(USER);
        IERC20(Mainnet.WETH).approve(Mainnet.ROUTER02, type(uint256).max);
        uint256 u0 = IERC20(Mainnet.USDC).balanceOf(USER);
        uint256 w0 = IERC20(Mainnet.WETH).balanceOf(USER);
        uint256 p0 = IERC20(Mainnet.WETH).balanceOf(POOL_500);

        (bool ok, ) = Mainnet.ROUTER02.call(Answer.CALLDATA);
        assertTrue(ok, "calldata reverted on SwapRouter02");
        vm.stopPrank();

        assertEq(w0 - IERC20(Mainnet.WETH).balanceOf(USER), 2 ether, "must spend exactly 2 WETH");
        assertEq(IERC20(Mainnet.WETH).balanceOf(POOL_500) - p0, 2 ether, "swap did not go through the 0.05% pool");
        assertGt(IERC20(Mainnet.USDC).balanceOf(USER) - u0, 3400e6, "USDC out too low");
    }
}
