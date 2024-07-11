from typing import List

from ..database import db_ops

from ..models.models import Customer

def get_customers(customer: Customer) -> List[Customer]:
    customers = db_ops.get_customers(customer)
    return list(customers.values())