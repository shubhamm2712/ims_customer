from typing import List, Dict

from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.models import Customer
from ..exceptions import UnauthorizedException

def set_org_model(customer: Customer, auth_result: Dict) -> Customer:
    if ORG in auth_result:
        customer.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return customer

def set_org_multiple_model(customers: List[Customer], auth_result: Dict) -> List[Customer]:
    if ORG in auth_result:
        for customer in customers:
            customer.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return customers