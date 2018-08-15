pragma solidity ^0.4.20;

import "./Ownable.sol";
import "./SearchContract.sol";

contract IdContract is Ownable {

    string private id;
    string private dbUrl;

    mapping (address => bool) allowedUsers;

    modifier onlyAllowedUser() {
        require(allowedUsers[msg.sender] || msg.sender == owner, "Sender unauthorized");
        _;
    }

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

    function getId() external view onlyAllowedUser returns(string) {
        return id;
    }

    function getDbUrl() external view onlyAllowedUser returns(string) {
        return dbUrl;
    }

    function registerAllowedUser(address _user) external onlyOwner {
        allowedUsers[_user] = true;
    }

    function deregisterAllowedUser(address _user) external onlyOwner {
        allowedUsers[_user] = false;
    }
} 
