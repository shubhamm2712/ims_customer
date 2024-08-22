from sqlmodel import Session

from ..config import engine

from ..models.models import Customer

class CreateCustomerDB:
    def add_customer(customer: Customer) -> Customer:
        with Session(engine) as session:
            session.add(customer)
            session.commit()
            session.refresh(customer)
            return customer