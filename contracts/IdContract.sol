pragma solidity ^0.4.20;

import "./Ownable.sol";
import "./SearchContract.sol";

contract IdContract is Ownable {

    string public id;
    string public dbUrl;

    constructor(string _id, string _dbUrl, address _searchAddress) public {
        setId(_id, _searchAddress);
        dbUrl = _dbUrl;
    }

    function setId(string _id, address _searchAddress) public onlyOwner {
        SearchContract(_searchAddress).setLink(keccak256(abi.encodePacked(_id)));
        id = _id;
    }

    function deleteId(address _searchAddress) external onlyOwner {
        SearchContract(_searchAddress).deleteLink(keccak256(abi.encodePacked(id)));
        id = "";
    }
} 
