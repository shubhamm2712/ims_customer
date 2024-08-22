from sqlmodel import Session, select, update

from typing import Optional, List

from ..config.consts import ACTIVE_ID_NOT_FOUND

from ..config import engine

from ..models.models import Customer

class UpdateCustomerDB:
    def update_customer(customer: Customer) -> Customer:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.id == customer.id, Customer.org == customer.org, Customer.active == 1)
            results = session.exec(statement)
            db_customer = results.first()
            if db_customer is None:
                return None
            db_customer.update_data(customer)
            session.add(db_customer)
            session.commit()
            session.refresh(db_customer)
            return db_customer

    def deactivate_customers(customer_org: str, customer_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = update(Customer).where(Customer.id.in_(customer_ids), Customer.org == customer_org, Customer.usedInTransaction == 0).values(active = 0)
            session.exec(statement)
            session.commit()
    
    def recover_customers(customer_org: str, customer_ids: List[int]) -> None:
        with Session(engine) as session:
            statement = update(Customer).where(Customer.id.in_(customer_ids), Customer.org == customer_org, Customer.active == 0).values(active = 1)
            session.exec(statement)
            session.commit()

    def update_customer_in_trans(customer: Customer, in_trans: int) -> Optional[Customer]:
        with Session(engine) as session:
            statement = select(Customer).where(Customer.id == customer.id, Customer.org == customer.org)
            results = session.exec(statement)
            db_customer = results.first()
            if db_customer is None:
                return None
            db_customer.usedInTransaction = in_trans
            db_customer.active = 1
            session.add(db_customer)
            session.commit()
            session.refresh(db_customer)
            return db_customer