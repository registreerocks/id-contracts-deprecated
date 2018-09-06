from .authentication import requires_auth, requires_scope
from .transaction_functions import (_claim_ownership, _delete_id,
                                    _deploy_id_contract,
                                    _deregister_allowed_user,
                                    _get_id_contract_address,
                                    _get_identifying_id, _get_identifying_ids,
                                    _register_allowed_user, _set_id,
                                    _set_id_after_deletion)

@requires_auth
@requires_scope('admin')
def deploy_id_contract(body):
    return _deploy_id_contract(body.get('id'), body.get('db_url'))

@requires_auth
@requires_scope('student')
def set_id(body):
    return _set_id(body.get('current_id'), body.get('new_id'))

@requires_auth
@requires_scope('student')
def delete_id(body):
    return _delete_id(body.get('id'))

@requires_auth
@requires_scope('student')
def set_id_after_deletion(body):
    return _set_id_after_deletion(body.get('address'), body.get('id'))

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_id_contract_address(id):
    return _get_id_contract_address(id)

@requires_auth
@requires_scope('admin', 'lecturer', 'student')
def get_identifying_id(address):
    return _get_identifying_id(address)

@requires_auth
@requires_scope('admin', 'lecturer')
def get_identifying_ids(body):
    return _get_identifying_ids(body.get('addresses'))

@requires_auth
@requires_scope('student')
def claim_ownership(body):
    return _claim_ownership(body.get('contract_address'), body.get('new_owner'))

@requires_auth
@requires_scope('admin', 'student')
def register_allowed_user(body):
    return _register_allowed_user(body.get('contract_address'), body.get('user_address'))

@requires_auth
@requires_scope('admin', 'student')
def deregister_allowed_user(body):
    return _deregister_allowed_user(body.get('contract_address'), body.get('user_address'))