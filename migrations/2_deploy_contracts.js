var Ownable = artifacts.require("./Ownable.sol");
var IdContract = artifacts.require("./IdContract.sol");
var SearchContract = artifacts.require("./SearchContract.sol");

module.exports = function(deployer) {
    deployer.deploy(Ownable);
    deployer.deploy(IdContract, "001"); // "001" for testing
    deployer.deploy(SearchContract);
};