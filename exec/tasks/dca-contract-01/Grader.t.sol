// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IERC20} from "../../src/Common.sol";
import {DCA} from "../../src/Submission.sol";

contract Grader is Test {
    DCA dca;
    address owner  = address(this);
    address outsider = address(0xBEEF);

    function setUp() public {
        dca = new DCA(Mainnet.ROUTER02, Mainnet.USDC, Mainnet.WETH, 500);
        deal(Mainnet.USDC, owner, 10_000e6);
        IERC20(Mainnet.USDC).approve(address(dca), type(uint256).max);
    }

    function test_deposit_and_buy() public {
        dca.deposit(5_000e6);
        assertEq(IERC20(Mainnet.USDC).balanceOf(address(dca)), 5_000e6, "deposit did not pull USDC");

        dca.buy(1_000e6, 0);
        assertEq(IERC20(Mainnet.USDC).balanceOf(address(dca)), 4_000e6, "buy did not spend exactly amountIn");
        assertGt(IERC20(Mainnet.WETH).balanceOf(address(dca)), 0.3 ether, "buy produced no/too little WETH");
    }

    function test_only_owner_can_buy() public {
        dca.deposit(5_000e6);
        vm.prank(outsider);
        vm.expectRevert();
        dca.buy(1_000e6, 0);
    }

    function test_only_owner_can_withdraw() public {
        dca.deposit(5_000e6);
        vm.prank(outsider);
        vm.expectRevert();
        dca.withdraw(Mainnet.USDC, 1_000e6);
    }

    function test_owner_withdraw_works() public {
        dca.deposit(5_000e6);
        uint256 b0 = IERC20(Mainnet.USDC).balanceOf(owner);
        dca.withdraw(Mainnet.USDC, 2_000e6);
        assertEq(IERC20(Mainnet.USDC).balanceOf(owner) - b0, 2_000e6, "withdraw did not pay the owner");
    }
}
