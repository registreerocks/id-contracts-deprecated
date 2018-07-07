var SearchContract = artifacts.require("./SearchContract.sol");

contract('SearchContract', function (accounts) {
    it("should have no address for id 1", function () {
        return SearchContract.deployed().then(function (instance) {
            return instance.idcontracts(1);
        }).then(function (address) {
            assert.equal(address, 0x0, "address is not 0x0");
        });
    });

    it("should set the address to 0xa for id 1", function () {
        var SearchContractInstance;
        return SearchContract.deployed().then(function (instance) {
            SearchContractInstance = instance;
            return SearchContractInstance.setLink(
                1,
                { "from": accounts[0] }
            );
        }).then(function () {
            return SearchContractInstance.idcontracts(1);
        }).then(function (address) {
            assert.equal(address, accounts[0], "address is not coinbase");
        });
    });

    it("should revert the transaction due to invalid message sender", function () {
        var SearchContractInstance;
        return SearchContract.deployed().then(function (instance) {
            SearchContractInstance = instance;
            return SearchContractInstance.deleteLink(
                1,
                { "from": accounts[1] }
            );
        }).then(assert.fail)
            .catch(function (error) {
                assert.include(error.message, 'revert', 'transaction was not reverted');
            });
    });

    it("should remove the address of id 1", function () {
        var SearchContractInstance;
        return SearchContract.deployed().then(function (instance) {
            SearchContractInstance = instance;
            return SearchContractInstance.deleteLink(
                1,
                { "from": accounts[0] }
            );
        }).then(function () {
            return SearchContractInstance.idcontracts(1);
        }).then(function (address) {
            assert.equal(address, 0x0, "address is not 0x0");
        });
    });
});