from .utils import get_remote_accounts


def test_gas_variation(web3, contracts, local_accounts, std_tx):
    """ Use GasVariation contract to test a full range of gas usage """

    owner, joe = get_remote_accounts(web3, 2)

    gv = contracts.get('GasVariation')
    assert gv.address is not None

    # Low gas
    hsh = gv.functions.low_gas().transact(std_tx({
            'from': joe,
            'gas': int(1e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1

    # Med gas
    hsh = gv.functions.med_gas().transact(std_tx({
            'from': joe,
            'gas': int(2e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1

    # High gas
    hsh = gv.functions.high_gas().transact(std_tx({
            'from': joe,
            'gas': int(5e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1

    # Error gas
    hsh = gv.functions.error_gas().transact(std_tx({
            'from': joe,
            'gas': int(6e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1


def test_gas_variation_caller(web3, contracts, local_accounts, std_tx):
    """ Use GasVariation contract to test a full range of gas usage """

    owner, joe = get_remote_accounts(web3, 2)

    gv = contracts.get('GasVariation')
    assert gv.address is not None
    gvc = contracts.get('GasVariationCaller')
    assert gvc.address is not None
    assert gvc.functions.getGasVariationAddress().call() == gv.address, (
        "GasVariation address not set"
    )

    # Low gas
    hsh = gvc.functions.callLowGas().transact(std_tx({
            'from': joe,
            'gas': int(1e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1

    # Med gas
    hsh = gvc.functions.callMedGas().transact(std_tx({
            'from': joe,
            'gas': int(2e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1
