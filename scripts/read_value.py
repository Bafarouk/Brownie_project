from brownie import SimpleStorage, config


def read_value():
    # -1: the recent contract deployed / 0 : the frist contract deployed
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retreive())


def main():
    read_value()
