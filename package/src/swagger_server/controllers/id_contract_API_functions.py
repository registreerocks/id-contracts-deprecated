from .transaction_functions import (_delete_id, _deploy_id_contract, _set_id,
                                    _set_id_after_deletion)


def deploy_id_contract(body):
    return _deploy_id_contract(body.get('id'))

def set_id(body):
    return _set_id(body.get('current_id'), body.get('new_id'))

def delete_id(body):
    return _delete_id(body.get('id'))

def set_id_after_deletion(body):
    return _set_id_after_deletion(body.get('address'), body.get('id'))