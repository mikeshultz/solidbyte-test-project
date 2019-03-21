import interface.IGasVariationVyper as IGasVariation

implements: IGasVariation

owner: public(address)
counter: public(uint256)

LOW_GAS_LOOPS: constant(uint256) = 10
MED_GAS_LOOPS: constant(uint256) = 25
HIGH_GAS_LOOPS: constant(uint256) = 175
ERROR_GAS_LOOPS: constant(uint256) = 900


@public
def __init__():
    self.owner = msg.sender


@public
def low_gas() -> uint256:
    for i in range(LOW_GAS_LOOPS):
        self.counter += 1
    return self.counter


@public
def med_gas() -> uint256:
    for i in range(MED_GAS_LOOPS):
        self.counter += 1
    return self.counter


@public
def high_gas() -> uint256:
    for i in range(HIGH_GAS_LOOPS):
        self.counter += 1
    return self.counter


# This will fail on Ropsten
@public
def error_gas() -> uint256:
    for i in range(ERROR_GAS_LOOPS):
        self.counter += 1
    return self.counter
