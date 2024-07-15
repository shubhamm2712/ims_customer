from typing import Union

from ..config.consts import ORG, ORG_NOT_FOUND
from ..models.models import Customer, Broker
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def set_org_model(cust_brok: Union[Customer, Broker], auth_result: dict) -> Union[Customer, Broker]:
    if ORG in auth_result:
        cust_brok.org = auth_result[ORG]
    if not cust_brok.org:
        raise InvalidBodyException(ORG_NOT_FOUND)
    return cust_brok