pragma solidity >=0.4.22 <0.7.0;

interface IGasVariation {
    function owner() external returns (address);
    function low_gas() external returns (uint256);
    function med_gas() external returns (uint256);
    function high_gas() external returns (uint256);
    function error_gas() external returns (uint256);
}
