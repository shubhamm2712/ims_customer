from typing import List, Optional

from ..config.consts import CUSTOMER_DOES_NOT_EXIST

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer, SingleEntity

def get_customers(customer: Customer) -> List[Customer]:
    customers = db_ops.get_customers(customer)
    return list(customers.values())

def get_customer(customer: Customer) -> Optional[SingleEntity]:
    customer_entity = db_ops.get_customer(customer)
    if customer_entity.customer is None:
        raise InvalidBodyException(CUSTOMER_DOES_NOT_EXIST)
    return customer_entity