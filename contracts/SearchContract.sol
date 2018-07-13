pragma solidity ^0.4.20;

contract SearchContract {

    mapping (bytes32 => address) public idcontracts;

    function setLink(bytes32 _id) external {
        idcontracts[_id] = msg.sender;
    }

    function deleteLink(bytes32 _id) external {
        require (idcontracts[_id] == msg.sender);
        idcontracts[_id] = 0x0;
    }
} 