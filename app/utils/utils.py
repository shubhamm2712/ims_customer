from typing import Union, List, Dict

from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.models import Customer
from ..exceptions import UnauthorizedException

def set_org_model(cust_brok: Customer, auth_result: Dict) -> Customer:
    if ORG in auth_result:
        cust_brok.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return cust_brok

def set_org_multiple_model(cust_broks: List[Customer], auth_result: Dict) -> List[Customer]:
    if ORG in auth_result:
        for cust_brok in cust_broks:
            cust_brok.org = auth_result[ORG]
    else:
        raise UnauthorizedException(ORG_NOT_FOUND)
    return cust_broks