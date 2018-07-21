import os

from Crypto.Hash import keccak
from web3 import HTTPProvider, Web3

from .contracts import id_contract_interface, search_contract_interface

W3 = Web3(HTTPProvider('http://' + os.getenv('RPC_HOST')+':'+os.getenv('RPC_PORT')))
SEARCH_CONTRACT_ADDRESS = Web3.toChecksumAddress(os.getenv('SEARCH_CONTRACT'))

def _deploy_id_contract(_id):
    IdContract = W3.eth.contract(abi=id_contract_interface['abi'], bytecode=id_contract_interface['bytecode'])
    tx_hash = IdContract.constructor(_id, SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
    tx_receipt = W3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt.contractAddress

def _set_id(_id, new_id):
    id_contract = _get_id_contract(_id)
    try:
        id_contract.functions.deleteId(SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        id_contract.functions.setId(new_id, SEARCH_CONTRACT_ADDRESS).transact({'from': W3.eth.accounts[0]})
        return True
    except ValueError:
        return {'ERROR': 'No contract corresponding to this id found.'}, 400

def _delete_id(_id):
    id_contract = _get_id_contract(_id)
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

def _get_id_contract(_id):
    search_contract = W3.eth.contract(address=SEARCH_CONTRACT_ADDRESS, abi=search_contract_interface['abi'])
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(_id.encode())
    id_contract_address = search_contract.functions.idcontracts(keccak_hash.hexdigest()).call()
    return id_contract_address
