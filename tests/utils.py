""" Test utilities """


def get_remote_accounts(web3, total=6):
    """
    Return 6 accounts

    (admin, bidder, hoster, validator1, validator2, validator3,
     validator4) = get_accounts()
    """
    return [web3.eth.accounts[i] for i in range(0, total)]
