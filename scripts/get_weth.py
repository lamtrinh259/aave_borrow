from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    """
    Runs the get_weth function to get WETH
    """
    get_weth()


def get_weth():
    """Mints WETH by depositing ETH"""
    ## WETH contract on Goerli: https://goerli.etherscan.io/token/0xb4fbf271143f4fbf7b91a5ded31805e42b2208d6#writeContract
    # Need ABI
    # Need address
    account = get_account()
    weth = interface.iWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
    tx.wait(1)
    print("received 0.1 WETH")
    return tx
