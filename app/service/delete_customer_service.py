from typing import List

from ..database import DeleteCustomerDB

from ..models.models import Customer

class DeleteCustomerService:

    def delete_customers(customers: List[Customer]) -> None:
        if not customers:
            return
        customer_org = customers[0].org
        customer_ids = [customer.id for customer in customers]
        DeleteCustomerDB.delete_customers(customer_org, customer_ids)