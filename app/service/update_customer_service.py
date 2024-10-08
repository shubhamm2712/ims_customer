from typing import List

from ..config.consts import CANNOT_BE_USED_IN_TRANSACTION, CANNOT_BE_ROLLBACKED_IN_TRANSACTION

from ..database import UpdateCustomerDB

from ..exceptions import InvalidBodyException

from ..models.models import Customer

class UpdateCustomerService:
    def deactivate_customers(customers: List[Customer]) -> None:
        if not customers:
            return
        customer_org = customers[0].org
        customer_ids = [customer.id for customer in customers]
        UpdateCustomerDB.deactivate_customers(customer_org, customer_ids)
    
    def recover_customers(customers: List[Customer]) -> None:
        if not customers:
            return
        customer_org = customers[0].org
        customer_ids = [customer.id for customer in customers]
        UpdateCustomerDB.recover_customers(customer_org, customer_ids)

    def customer_in_transaction(customer: Customer) -> Customer:
        db_customer = UpdateCustomerDB.add_customer_in_trans(customer)
        if db_customer is None:
            raise InvalidBodyException(CANNOT_BE_USED_IN_TRANSACTION)
        return db_customer

    def customer_rollback_in_trans(customer: Customer) -> Customer:
        db_customer = UpdateCustomerDB.rollback_customer_in_trans(customer)
        if db_customer is None:
            raise InvalidBodyException(CANNOT_BE_ROLLBACKED_IN_TRANSACTION)
        return db_customer