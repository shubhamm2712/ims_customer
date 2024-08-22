from sqlmodel import Session, delete

from typing import List

from ..config import engine

from ..models.models import Customer

class DeleteCustomerDB:
    def delete_customers(customer_org: str, customer_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = delete(Customer).where(Customer.id.in_(customer_ids), Customer.org == customer_org, Customer.active == 0)
            session.exec(statement)
            session.commit()