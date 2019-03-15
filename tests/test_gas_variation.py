from .utils import std_tx, get_remote_accounts

def test_gas_variation(web3, contracts, local_accounts):
    """ Use GasVariation contract to test a full range of gas usage """

    owner, joe = get_remote_accounts(web3, 2)
    
    gv = contracts.get('GasVariation')
    assert gv.address is not None

    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    # Low gas
    hsh = gv.functions.low_gas().transact(std_tx({
            'from': joe,
            'gas': int(1e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1
    print("low_gas() gasUsed: ", receipt.gasUsed)

    # Med gas
    hsh = gv.functions.med_gas().transact(std_tx({
            'from': joe,
            'gas': int(2e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1
    print("med_gas() gasUsed: ", receipt.gasUsed)

    # High gas
    hsh = gv.functions.high_gas().transact(std_tx({
            'from': joe,
            'gas': int(5e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1
    print("high_gas() gasUsed: ", receipt.gasUsed)

    # Error gas
    hsh = gv.functions.error_gas().transact(std_tx({
            'from': joe,
            'gas': int(6e6),
        }))
    receipt = web3.eth.waitForTransactionReceipt(hsh)
    assert receipt.status == 1
    print("error_gas() gasUsed: ", receipt.gasUsed)
