pragma solidity ^0.4.20;

import "./Ownable.sol";
import "./SearchContract.sol";

contract IdContract is Ownable {

    string public id;

    constructor(string _id, address _searchAddress) public {
        setId(_id, _searchAddress);
    }

    function setId(string _id, address _searchAddress) public onlyOwner {
        SearchContract(_searchAddress).setLink(uint(keccak256(_id)));
        id = _id;
    }

    function deleteId(address _searchAddress) external onlyOwner {
        SearchContract(_searchAddress).deleteLink(uint(keccak256(id)));
        id = "";
    }
} 
