pragma solidity >=0.4.22 <0.7.0;

import "./interface/IGasVariation.sol";

contract GasVariationCaller {

    IGasVariation gasVariation;

    constructor(address gasVariationAddress) public
    {
        gasVariation = IGasVariation(gasVariationAddress);
    }

    function callLowGas() public returns (uint256)
    {
        return gasVariation.low_gas();
    }

    function callMedGas() public returns (uint256)
    {
        return gasVariation.med_gas();
    }

    function getGasVariationAddress() public view returns (address)
    {
        return address(gasVariation);
    }

}
