from typing import Union

from ..config.consts import NAME_NOT_FOUND, ID_NOT_FOUND, INVALID_PRODUCT_DETAILS_TYPE
from ..models.models import Customer, Broker
from ..exceptions.invalid_body_exceptions import InvalidBodyException

def sanitize_customer(customer: Customer) -> None:
    if customer.id is not None:
        if type(customer.id) != int:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
    if customer.name is not None:
        if type(customer.name) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            customer.name = customer.name.strip()
            if customer.name == "":
                customer.name = None
    if customer.address is not None:
        if type(customer.address) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            customer.address = customer.address.strip()
            if customer.address == "":
                customer.address = None
    if customer.phone is not None:
        if type(customer.phone) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            customer.phone = customer.phone.strip()
            if customer.phone == "":
                customer.phone = None
    if customer.taxNumber is not None:
        if type(customer.taxNumber) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            customer.taxNumber = customer.taxNumber.strip()
            if customer.taxNumber == "":
                customer.taxNumber = None
    
def sanitize_broker(broker: Broker) -> None:
    if broker.id is not None:
        if type(broker.id) != int:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
    if broker.name is not None:
        if type(broker.name) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            broker.name = broker.name.strip()
            if broker.name == "":
                broker.name = None
    if broker.phone is not None:
        if type(broker.phone) != str:
            raise InvalidBodyException(INVALID_PRODUCT_DETAILS_TYPE)
        else:
            broker.phone = broker.phone.strip()
            if broker.phone == "":
                broker.phone = None
    
def sanitize(cust_brok : Union[Customer, Broker]) -> None:
    if type(cust_brok) == Customer:
        sanitize_customer(cust_brok)
    else:
        sanitize_broker(cust_brok)

def add_validator(cust_brok: Union[Customer, Broker]) -> Union[Customer, Broker]:
    sanitize(cust_brok)
    if cust_brok.name is None:
        raise InvalidBodyException(NAME_NOT_FOUND)
    return cust_brok

def del_validator(cust_brok: Union[Customer, Broker]) -> Union[Customer, Broker]:
    sanitize(cust_brok)
    if cust_brok.id is None:
        raise InvalidBodyException(ID_NOT_FOUND)
    return cust_brok