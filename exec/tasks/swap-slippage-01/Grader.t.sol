// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {Answer} from "../../src/Answer.sol";

interface IRouter {
    struct P { address tokenIn; address tokenOut; uint24 fee; address recipient;
               uint256 amountIn; uint256 amountOutMinimum; uint160 sqrtPriceLimitX96; }
    function exactInputSingle(P calldata) external payable returns (uint256);
}

/// A swap is only correct if its slippage guard actually binds. Executing the
/// calldata on a clean fork cannot tell a real guard from amountOutMinimum=0,
/// so we run it twice: once clean (must succeed) and once after an adversary
/// moves the price ~4% against it (must revert).
contract Grader is Test {
    address constant USER = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
    address constant ADVERSARY = address(0xADD);

    function _arm(address who) internal {
        deal(Mainnet.WETH, who, 20_000 ether);
        vm.prank(who);
        IERC20(Mainnet.WETH).approve(Mainnet.ROUTER02, type(uint256).max);
    }

    function test_executes_cleanly() public {
        _arm(USER);
        uint256 u0 = IERC20(Mainnet.USDC).balanceOf(USER);
        vm.prank(USER);
        (bool ok, ) = Mainnet.ROUTER02.call(Answer.CALLDATA);
        assertTrue(ok, "calldata reverted on an unmoved market");
        assertGt(IERC20(Mainnet.USDC).balanceOf(USER) - u0, 18_900e6, "output too low - wrong pool or size");
    }

    function test_slippage_guard_binds() public {
        _arm(ADVERSARY);
        vm.prank(ADVERSARY);
        IRouter(Mainnet.ROUTER02).exactInputSingle(
            IRouter.P(Mainnet.WETH, Mainnet.USDC, 500, ADVERSARY, 3_000 ether, 0, 0));

        _arm(USER);
        vm.prank(USER);
        (bool ok, ) = Mainnet.ROUTER02.call(Answer.CALLDATA);
        assertFalse(ok, "no real slippage guard - the swap still filled after a 4% adverse move");
    }
}
