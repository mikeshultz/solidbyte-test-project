# Vyper Interface for GasVariationCaller
@public
def owner() -> address: constant

@public
def low_gas() -> uint256: constant

@public
def med_gas() -> uint256: constant

@public
def high_gas() -> uint256: constant

@public
def error_gas() -> uint256: constant
