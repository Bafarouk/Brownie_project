from brownie import SimpleStorage, accounts, config, network
import os


def deploy_simple_storage():
    # getting the first address from 10 accounts that fanache generate :
    # account = accounts[0]

    # getting account from the aded accounts with CLI ( DON'T DORGET THE PASSWORD ) :
    # account = accounts.load("farouk-account")

    # getting with the .env meth2 with wallets :
    # account = accounts.add(config["wallets"]["from_key"])

    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retreive()
    print(stored_value)
    transaction = simple_storage.store(33, {"from": account})
    transaction.wait(1)
    updated_value_stored = simple_storage.retreive()
    print(updated_value_stored)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
