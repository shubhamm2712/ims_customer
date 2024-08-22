from typing import List

from ..config.consts import NAME_NOT_FOUND, ID_NOT_FOUND, INVALID_CUSTOMER_DETAILS_TYPE
from ..models.models import Customer
from ..exceptions import InvalidBodyException

class CustomerValidators:
    def sanitize(customer: Customer) -> None:
        if customer.id is not None:
            if type(customer.id) != int:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
        if customer.name is not None:
            if type(customer.name) != str:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
            else:
                customer.name = customer.name.strip()
                if customer.name == "":
                    customer.name = None
        if customer.address is not None:
            if type(customer.address) != str:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
            else:
                customer.address = customer.address.strip()
                if customer.address == "":
                    customer.address = None
        if customer.phone is not None:
            if type(customer.phone) != str:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
            else:
                customer.phone = customer.phone.strip()
                if customer.phone == "":
                    customer.phone = None
        if customer.taxNumber is not None:
            if type(customer.taxNumber) != str:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
            else:
                customer.taxNumber = customer.taxNumber.strip()
                if customer.taxNumber == "":
                    customer.taxNumber = None
        if customer.metaData is not None:
            if type(customer.metaData) != str:
                raise InvalidBodyException(INVALID_CUSTOMER_DETAILS_TYPE)
            else:
                customer.metaData = customer.metaData.strip()
                if customer.metaData == "":
                    customer.metaData = None
    
    def add_validator(customer: Customer) -> Customer:
        CustomerValidators.sanitize(customer)
        if customer.name is None:
            raise InvalidBodyException(NAME_NOT_FOUND)
        return customer
    
    def id_validator(customer: Customer) -> Customer:
        CustomerValidators.sanitize(customer)
        if customer.id is None:
            raise InvalidBodyException(ID_NOT_FOUND)
        return customer
    
    def list_id_validator(customers: List[Customer]) -> List[Customer]:
        for customer in customers:
            CustomerValidators.id_validator(customer)
        return customers