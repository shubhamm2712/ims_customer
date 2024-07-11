from ..config.consts import ID_NOT_FOUND

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer

def is_update(customer: Customer) -> bool:
    if customer.id:
        return True
    return False

def validate_update_customer(customer: Customer) -> None:
    cust_ids = db_ops.get_customer_ids(customer)
    if customer.id not in cust_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def add_customer(customer: Customer) -> None:
    isUpdate = is_update(customer)
    if isUpdate:
        validate_update_customer(customer)
        db_ops.update_customer(customer)
    else:
        db_ops.add_customer(customer)
