STD_GAS = int(1e5)
STD_GAS_PRICE = int(3e9)  # 3gwei

def std_tx(tx):
    """ Build a standard tx object """
    std = {
        'gas': STD_GAS,
        'gasPrice': STD_GAS_PRICE,
    }
    std.update(tx)
    return std


def get_remote_accounts(web3, total=6):
    """
    Return 6 accounts

    admin, bidder, hoster, validator1, validator2, validator3, validator4 = get_accounts()
    """
    return [web3.eth.accounts[i] for i in range(0, total)]