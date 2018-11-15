var IdContract = artifacts.require("./IdContract.sol");
var SearchContract = artifacts.require("./SearchContract.sol");

const {
    expectThrow
} = require('openzeppelin-solidity/test/helpers/expectThrow');
const {
    EVMRevert
} = require('openzeppelin-solidity/test/helpers/EVMRevert');

contract('IdContract', function(accounts) {

    it("should not be queriable", function() {
        var IdContractInstance;
        return IdContract.deployed().then(async function(instance) {
            IdContractInstance = instance;
            return IdContractInstance.isQueriable();
        }).then(function(isQ) {
            assert.equal(isQ, false, "student contract not queriable");
        }).then(function() {
            expectThrow(IdContractInstance.getId(), EVMRevert);
        });
    });

    it("should make contract queriable", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return IdContractInstance.toggleQueriability({from: accounts[0]});
        }).then(function() {
            return IdContractInstance.isQueriable();
        }).then(function(isQ) {
            assert.equal(isQ, true, "student contract not queriable");
        });
    });

    it("should set the initial id on deployment", function() {
        return IdContract.deployed().then(function(instance) {
            return instance.getId();
        }).then(function(id) {
            assert.equal(id, "001", "id was not properly set on initialization");
        });
    });

    it("should not return id because not allowed user", function() {
        return IdContract.deployed().then(function(instance) {
            expectThrow(instance.getId({from: accounts[1]}), EVMRevert);
        });
    });

    it("should not return db url because not allowed user", function() {
        return IdContract.deployed().then(function(instance) {
            expectThrow(instance.getDbUrl({from: accounts[1]}), EVMRevert);
        });
    });

    it("should return db url", function() {
        return IdContract.deployed().then(function(instance) {
            return instance.getDbUrl({from: accounts[0]});
        }).then(function(url) {
            assert.equal(url, "www.example.com", "wrong url returned");
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
            return IdContractInstance.getId();
        }).then(function(id) {
            assert.equal(id, "002", "id was not properly set");
        });
    });

    it("should not set the id because not owner", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return SearchContract.deployed().then(function(instance){
                expectThrow(IdContractInstance.setId(
                    "002",
                    instance.address,
                    {"from": accounts[1]}
                ), EVMRevert);
            })
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
            return IdContractInstance.getId();
        }).then(function(id) {
            assert.equal(id, "", "id was not properly removed");
        });
    });

    it("should register and deregister an allowed user", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return IdContractInstance.allowedUsers(accounts[1]);
        }).then(function(response) {
            assert.equal(response, false, 'user already registered')
        }).then(function() {
            return IdContractInstance.registerAllowedUser(accounts[1], {from: accounts[0]});
        }).then(function() {
            return IdContractInstance.allowedUsers(accounts[1]);
        }).then(function(response) {
            assert.equal(response, true, 'user not registered');
        }).then(function() {
            return IdContractInstance.deregisterAllowedUser(accounts[1], {from: accounts[0]});
        }).then(function() {
            return IdContractInstance.allowedUsers(accounts[1]);
        }).then(function(response) {
            assert.equal(response, false, 'user still registered');
        });
    });

    it("should make contract non-queriable", function() {
        var IdContractInstance;
        return IdContract.deployed().then(function(instance) {
            IdContractInstance = instance;
            return IdContractInstance.toggleQueriability({from: accounts[0]});
        }).then(function() {
            return IdContractInstance.isQueriable();
        }).then(function(isQ) {
            assert.equal(isQ, false, "student contract queriable");
        });
    });
});