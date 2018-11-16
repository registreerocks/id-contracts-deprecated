import os

from Crypto.Hash import keccak
from web3 import HTTPProvider, Web3

from .contracts import id_contract_interface, search_contract_interface

W3 = Web3(HTTPProvider('http://' + os.getenv('RPC_HOST')+':'+os.getenv('RPC_PORT')))
SEARCH_CONTRACT_ADDRESS = Web3.toChecksumAddress(os.getenv('SEARCH_CONTRACT'))

def _deploy_id_contract(_id, db_url):
    IdContract = W3.eth.contract(abi=id_contract_interface['abi'], bytecode=id_contract_interface['bytecode'])
    tx_hash = IdContract.constructor(_id, db_url, SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
    tx_receipt = W3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt.contractAddress

def _set_id(_id, new_id):
    id_contract = W3.eth.contract(address=_get_id_contract_address(_id), abi=id_contract_interface['abi'])
    try:
        id_contract.functions.deleteId(SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        id_contract.functions.setId(new_id, SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        return True
    except ValueError:
        return {'ERROR': 'No contract corresponding to this id found.'}, 400

def _delete_id(_id):
    id_contract = W3.eth.contract(address=_get_id_contract_address(_id), abi=id_contract_interface['abi'])
    try:
        id_contract.functions.deleteId(SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        return True
    except:
        return {'ERROR': 'No contract corresponding to this id found.'}, 400

def _set_id_after_deletion(address, new_id):
    id_contract = W3.eth.contract(address=address, abi=id_contract_interface['abi'])
    try:
        id_contract.functions.setId(new_id, SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        return True
    except:
        return {'ERROR': 'No contract corresponding to this address found.'}, 400

def _get_id_contract_address(_id):
    search_contract = W3.eth.contract(address=SEARCH_CONTRACT_ADDRESS, abi=search_contract_interface['abi'])
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(_id.encode())
    id_contract_address = search_contract.functions.idcontracts(keccak_hash.hexdigest()).call()
    return id_contract_address

def _get_identifying_id(address):
    id_contract = W3.eth.contract(address=address, abi=id_contract_interface['abi'])
    try:
        _id = id_contract.functions.getId().call({'from': W3.eth.accounts[0]})
        db_url = id_contract.functions.getDbUrl().call({'from': W3.eth.accounts[0]})
        return {'id': _id, 'db_url': db_url}
    except:
        return {'ERROR': 'Sender unauthorized'}, 401

def _get_identifying_ids(addresses):
    _ids = dict()
    for address in addresses:
        _ids[address] = _get_identifying_id(address)
    return _ids

def _claim_ownership(contract_address, new_owner):
    id_contract = W3.eth.contract(address=contract_address, abi=id_contract_interface['abi'])
    old_owner = id_contract.functions.owner().call()
    id_contract.functions.registerAllowedUser(old_owner).transact({'from': W3.eth.accounts[0]})
    id_contract.functions.transferOwnership(new_owner).transact({'from': W3.eth.accounts[0]})
    return True

def _register_allowed_user(contract_address, user_address):
    id_contract = W3.eth.contract(address=contract_address, abi=id_contract_interface['abi'])
    try: 
        id_contract.functions.registerAllowedUser(user_address).transact({'from': W3.eth.accounts[0]})
        return True
    except:
        return {'ERROR': 'Sender unauthorized'}, 401

def _deregister_allowed_user(contract_address, user_address):
    id_contract = W3.eth.contract(address=contract_address, abi=id_contract_interface['abi'])
    try: 
        id_contract.functions.deregisterAllowedUser(user_address).transact({'from': W3.eth.accounts[0]})
        return True
    except:
        return {'ERROR': 'Sender unauthorized'}, 401

def _toggle_queriability(contract_address):
    id_contract = W3.eth.contract(address=contract_address, abi=id_contract_interface['abi'])
    try: 
        id_contract.functions.toggleQueriability().transact({'from': W3.eth.accounts[0]})
        return id_contract.functions.isQueriable().call({'from': W3.eth.accounts[0]})
    except:
        return {'ERROR': 'Sender unauthorized'}, 401

def _check_queriability(contract_address):
    id_contract = W3.eth.contract(address=contract_address, abi=id_contract_interface['abi'])
    try: 
        return id_contract.functions.isQueriable().call({'from': W3.eth.accounts[0]})
    except:
        return {'ERROR': 'Sender unauthorized'}, 401