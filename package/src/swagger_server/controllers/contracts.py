import json

with open('../contracts/IdContract.json', 'r') as f:
    id_contract_interface = json.load(f)

with open('../contracts/SearchContract.json', 'r') as f:
    search_contract_interface = json.load(f)