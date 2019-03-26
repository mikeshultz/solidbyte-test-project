from .utils import get_remote_accounts


def test_dumb_contract(web3, contracts, local_accounts, std_tx, get_event,
                       has_event):
    """ Tests for Dumbcontract """

    owner, joe, alice = get_remote_accounts(web3, 3)

    dumb = contracts.get('DumbContract')
    assert dumb is not None
    assert dumb.address is not None

    tx_hash = dumb.functions.emitAddress(alice).transact(std_tx({
        'from': joe,
    }))
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    assert receipt.status == 1
    assert has_event(dumb, 'AddressEvent', receipt)
    event_data = get_event(dumb, 'AddressEvent', receipt)
    assert event_data.args.val == alice

    emit_num = 123
    tx_hash = dumb.functions.emitUint256(emit_num).transact(std_tx({
        'from': joe,
    }))
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    assert receipt.status == 1
    assert has_event(dumb, 'Uint256Event', receipt)
    event_data = get_event(dumb, 'Uint256Event', receipt)
    assert event_data.args.val == emit_num
