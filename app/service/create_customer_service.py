from typing import Dict

import requests

from ..config.consts import ID_NOT_FOUND

from ..exceptions import InvalidBodyException

from ..models.models import Customer

from ..database import CreateCustomerDB, UpdateCustomerDB

class CreateCustomerService:
    def add_customer(customer: Customer, auth_result: Dict) -> Customer:
        if customer.id is None:
            return CreateCustomerDB.add_customer(customer)
        else:
            customer_entity: Customer = UpdateCustomerDB.update_customer(customer)
            if customer_entity is None:
                raise InvalidBodyException(ID_NOT_FOUND)
            if customer_entity.usedInTransaction == 1:
                print(auth_result)
                # TODO: Update this part
            return customer_entity