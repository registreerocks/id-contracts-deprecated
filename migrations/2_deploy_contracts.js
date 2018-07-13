var Ownable = artifacts.require("./Ownable.sol");
var IdContract = artifacts.require("./IdContract.sol");
var SearchContract = artifacts.require("./SearchContract.sol");

// module.exports = function(deployer) {
//     deployer.then(function() {
//         return deployer.deploy(Ownable);
//     }).then(function() {
//         return deployer.deploy(SearchContract);
//     }).then(function() {
//         return SearchContract.deployed();
//     }).then(function(instance) {
//         return deployer.deploy(IdContract, "001", instance.address); // "001" for testing
//     });
// };

module.exports = function(deployer) {
    deployer.deploy(SearchContract);
};