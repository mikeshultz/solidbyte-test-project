STD_GAS_PRICE = int(3e9)  # 3gwei


def autofund_account(web3, address, value):
    """ Automatically fund an account """
    assert isinstance(value, int)

    net_id = int(web3.net.version)
    balance = web3.eth.getBalance(address)

    if net_id > 100:
        # If this is the test network, make sure our deployment account is
        # funded
        if balance == 0:
            tx = web3.eth.sendTransaction({
                'from': web3.eth.accounts[0],  # The pre-funded test account
                'to': address,
                'value': value,
                'gasPrice': STD_GAS_PRICE,
                })
            receipt = web3.eth.waitForTransactionReceipt(tx)
            assert receipt.status == 1, "Funding deployer_account failed"
            balance = web3.eth.getBalance(address)
            assert balance >= value, "Funding of deployer_account too low"
    else:
        # Make sure deployer account has at least 0.5 ether
        assert balance > int(5e17), (
            "deployer account needs to be funded. want: {}. has: {}".format(
                int(5e17),
                balance
            )
        )


def main(web3, contracts, deployer_account):

    # Fund the deployer account if necessary(test networks only)
    autofund_account(web3, deployer_account, int(1e18))

    # Deploy GasVariation
    GasVariation = contracts.get('GasVariation')
    gv = GasVariation.deployed()
    assert gv.address is not None

    GasVariationCaller = contracts.get('GasVariationCaller')
    gvc = GasVariationCaller.deployed(gv.address)
    assert gvc.address is not None

    DumbContract = contracts.get('DumbContract')
    dumb = DumbContract.deployed()
    assert dumb.address is not None
