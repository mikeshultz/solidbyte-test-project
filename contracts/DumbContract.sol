pragma solidity >=0.4.22 <0.7.0;

/* 
 * DumContract is a contract that only fires events and has no state
 */
contract DumbContract {

    event AddressEvent(address val);
    event Uint256Event(uint256 val);

    function emitAddress(address value) public
    {
        emit AddressEvent(value);
    }

    function emitUint256(uint256 value) public
    {
        emit Uint256Event(value);
    }

}
