# Vyper Interface for GasVariationCaller
contract IGasVariation:
    def owner() -> address: constant
    def low_gas() -> uint256: constant
    def med_gas() -> uint256: constant
    def high_gas() -> uint256: constant
    def error_gas() -> uint256: constant
