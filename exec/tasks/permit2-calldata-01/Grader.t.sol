// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import {Test} from "forge-std/Test.sol";
import {Mainnet, IPermit2} from "../../src/Common.sol";
import {Answer} from "../../src/Answer.sol";

contract Grader is Test {
    address constant USER = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;

    function test_grade() public {
        vm.startPrank(USER);
        (bool ok, ) = Mainnet.PERMIT2.call(Answer.CALLDATA);
        assertTrue(ok, "calldata reverted on Permit2");
        vm.stopPrank();

        (uint160 amount, uint48 expiration, ) =
            IPermit2(Mainnet.PERMIT2).allowance(USER, Mainnet.USDC, Mainnet.UNIVERSAL_ROUTER);
        assertEq(uint256(amount), 1000e6, "allowance amount wrong");
        assertEq(uint256(expiration), 1893456000, "expiration wrong");
    }
}
