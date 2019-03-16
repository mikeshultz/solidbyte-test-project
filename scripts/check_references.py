""" This script just does some verification we might need to repeat in the future """

def check_references(web3, gasVariation, gasVariationCaller):
    """ Check the references between the gas variation contracts """

    gvAddress = gasVariationCaller.functions.getGasVariationAddress().call()
    return gvAddress == gasVariation.address

def main(web3, contracts):
    """ Function to be called by `sb script` command """

    gasVariation = contracts.get('GasVariation')
    gasVariationCaller = contracts.get('GasVariationCaller')

    assert gasVariation is not None, "GasVariation deployment not found"
    assert gasVariationCaller is not None, "GasVariationCaller deployment not found"

    return check_references(web3, gasVariation, gasVariationCaller)
