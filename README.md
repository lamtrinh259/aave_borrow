1. Swap our ETH for WETH
2. Deposit some ETH into AAVE
3. Borrow some asset with the ETH collateral
    3a. Sell the borrowed asset (short selling)
4. Repay everything back

Testing: 
- Integration test: Goerli
- Unit tests: Mainnet-fork (since we don't have oracles)