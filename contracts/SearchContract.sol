pragma solidity ^0.4.20;

contract SearchContract {

    mapping (uint => address) public idcontracts;

    function setLink(uint _id) external {
        idcontracts[_id] = msg.sender;
    }

    function deleteLink(uint _id) external {
        require (idcontracts[_id] == msg.sender);
        idcontracts[_id] = 0x0;
    }
} 