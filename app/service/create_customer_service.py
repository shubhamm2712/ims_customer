from typing import Dict, Optional

from ..config.consts import ID_NOT_FOUND

from ..exceptions import InvalidBodyException

from ..models.models import Customer

from ..database import CreateCustomerDB, UpdateCustomerDB

class CreateCustomerService:
    def add_customer(customer: Customer) -> Customer:
        if customer.id is None:
            return CreateCustomerDB.add_customer(customer)
        else:
            customer_entity: Optional[Customer] = UpdateCustomerDB.update_customer(customer)
            if customer_entity is None:
                raise InvalidBodyException(ID_NOT_FOUND)
            return customer_entity