
from sqlmodel import Session, select, or_

from typing import Optional, List

from ..config import engine

from ..models.models import Customer

class ReadCustomerDB:
    def get_customer_all_details(customer: Customer) -> Optional[Customer]:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.org == customer.org, Customer.id == customer.id)
            results = session.exec(statement)
            db_customer = results.first()
            if db_customer is None:
                return None
            return db_customer
    
    def get_all_customers(customer: Customer) -> List[Customer]:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.org == customer.org, Customer.active == 1)
            results = session.exec(statement)
            return results.all()
        
    def get_deleted_customers(customer: Customer) -> List[Customer]:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.org == customer.org, Customer.active == 0)
            results = session.exec(statement)
            return results.all()
    
    def get_customers_list(customer_org: str, customer_ids: List[int]) -> List[Customer]:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.org == customer_org, Customer.id.in_(customer_ids))
            results = session.exec(statement)
            return results.all()
        



