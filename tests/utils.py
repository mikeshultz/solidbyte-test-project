""" Test utilities """
from attrdict import AttrDict
from hexbytes import HexBytes
from web3 import Web3
from web3.utils.events import get_event_data

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


def topic_signature(abi):
    if abi.get('type') != 'event':
        return None
    args = ','.join([a.get('type') for a in abi.get('inputs')])
    sig = '{}({})'.format(abi.get('name'), args)
    return Web3.sha3(text=sig)


def event_topics(web3contract):
    """ Process a Web3.py Contract and return a dict of event topic sigs """
    contract_abi = web3contract.abi
    sigs = AttrDict({})

    for abi in contract_abi:
        if abi.type == 'event':
            sigs[abi.name] = topic_signature(abi)
    return sigs


def event_abi(contract_abi, name):
    """ Return the abi for a specific event """
    for abi in contract_abi:
        if abi.get('type') == 'event' and abi.get('name') == name:
            return abi
    return None


def get_event(web3contract, event_name, rcpt):
    print(rcpt)
    if len(rcpt.logs) < 1:
        return None

    abi = event_abi(web3contract.abi, event_name)

    for log in rcpt.logs:
        evnt_data = get_event_data(abi, log)
        return evnt_data
    return None


def has_event(web3contract, event_name, rcpt):
    abi = event_abi(web3contract.abi, event_name)
    if abi is None:
        raise ValueError("Did not find {} in contract ABI.".format(event_name))
    sig = HexBytes(topic_signature(abi).hex())
    for log in rcpt.logs:
        if len(log.topics) > 0 and log.topics[0] == sig:
            return True
    return False
