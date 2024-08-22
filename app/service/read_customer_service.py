from typing import List

from ..config.consts import CUSTOMER_DOES_NOT_EXIST

from ..models.models import Customer

from ..database import ReadCustomerDB

from ..exceptions import InvalidBodyException

class ReadCustomerService:
    def get_customer(customer: Customer) -> Customer:
        customer_entity = ReadCustomerDB.get_customer_all_details(customer)
        if customer_entity is None:
            raise InvalidBodyException(CUSTOMER_DOES_NOT_EXIST)
        return customer_entity
    
    def get_all_customers(customer: Customer) -> List[Customer]:
        customers = ReadCustomerDB.get_all_customers(customer)
        if customers is None:
            return []
        return customers
    
    def get_deleted_customers(customer: Customer) -> List[Customer]:
        customers = ReadCustomerDB.get_deleted_customers(customer)
        if customers is None:
            return []
        return customers
    
    def get_customers_list(customer_org: str, customer_ids: List[int]) -> List[Customer]:
        if not customer_ids:
            return []
        result_customers = ReadCustomerDB.get_customers_list(customer_org, customer_ids)
        if result_customers is None:
            return []
        return result_customers