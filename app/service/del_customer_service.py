from ..config.consts import ID_NOT_FOUND

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer

def validate_cust_id_db(customer: Customer) -> None:
    customer_ids = db_ops.get_customer_ids(customer)
    if customer.id not in customer_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def del_customer(customer: Customer) -> None:
    validate_cust_id_db(customer)
    db_ops.delete_customer(customer)
    