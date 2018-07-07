var IdContract = artifacts.require("./IdContract.sol");
var SearchContract = artifacts.require("./SearchContract.sol");

contract('IdContract', function(accounts) {
    it("should set the initial id on deployment", function() {
        return IdContract.deployed().then(function(instance) {
            return instance.id();
        }).then(function(id) {
            assert.equal(id, "001", "id was not properly set on initialization");
        });
    });

    it("should set the id upon request", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return SearchContract.deployed().then(function(instance){
                return IdContractInstance.setId(
                    "002",
                    instance.address,
                    {"from": accounts[0]}
                );
            })
        }).then(function() {
            return IdContractInstance.id();
        }).then(function(id) {
            assert.equal(id, "002", "id was not properly set");
        });
    });

    it("should delete the id upon request", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return SearchContract.deployed().then(function(instance) {
                return IdContractInstance.deleteId(
                    instance.address,
                    {"from": accounts[0]}
                );
            })
        }).then(function() {
            return IdContractInstance.id();
        }).then(function(id) {
            assert.equal(id, "", "id was not properly removed");
        });
    });
});