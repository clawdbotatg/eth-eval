// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// Shared mainnet addresses + minimal interfaces for the exec-track graders.
library Mainnet {
    address constant WETH   = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    address constant USDC   = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    address constant DAI    = 0x6B175474E89094C44Da98b954EedeAC495271d0F;
    address constant ROUTER02        = 0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45; // SwapRouter02
    address constant UNIVERSAL_ROUTER= 0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD;
    address constant PERMIT2         = 0x000000000022D473030F116dDEE9F6B43aC78BA3;
    address constant V3_FACTORY      = 0x1F98431c8aD98523631AE4a59f267346ea31F984;
    address constant NPM             = 0xC36442b4a4522E871399CD717aBDD847Ab11FE88; // NonfungiblePositionManager
}

interface IERC20 {
    function balanceOf(address) external view returns (uint256);
    function approve(address, uint256) external returns (bool);
    function transfer(address, uint256) external returns (bool);
    function decimals() external view returns (uint8);
}

interface IWETH is IERC20 {
    function deposit() external payable;
}

interface IUniV3Pool {
    function slot0() external view returns (
        uint160 sqrtPriceX96, int24 tick, uint16 obsIndex, uint16 obsCard,
        uint16 obsCardNext, uint8 feeProtocol, bool unlocked);
    function tickSpacing() external view returns (int24);
    function token0() external view returns (address);
    function token1() external view returns (address);
    function fee() external view returns (uint24);
}

interface IV3Factory {
    function getPool(address, address, uint24) external view returns (address);
}

interface IPermit2 {
    function allowance(address user, address token, address spender)
        external view returns (uint160 amount, uint48 expiration, uint48 nonce);
}
