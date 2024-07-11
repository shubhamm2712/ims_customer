from ..config.consts import ID_NOT_FOUND

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer

def is_update(customer: Customer) -> bool:
    if customer.id:
        return True
    return False

def validate_update_customer(customer: Customer) -> None:
    # Check if id is in db or not
    raise InvalidBodyException(ID_NOT_FOUND)
    return 

def add_customer(customer: Customer) -> None:
    isUpdate = is_update(customer)
    if isUpdate:
        validate_update_customer(customer)
        # update
    else:
        # add
        pass
