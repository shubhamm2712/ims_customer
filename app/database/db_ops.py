from sqlmodel import Session, select
from typing import Set, Dict, List

from .db_config import engine

from ..models.models import Customer, Broker

def get_customer_ids(customer: Customer) -> Set:
    customer_ids = set()
    with Session(engine) as session:
        statement = select(Customer.id).where(Customer.org == customer.org)
        results = session.exec(statement)
        for id in results:
            customer_ids.add(id)
    return customer_ids

def get_customers(customer: Customer) -> Dict:
    customers = dict()
    with Session(engine) as session:
        statement = select(Customer).where(Customer.org == customer.org)
        results = session.exec(statement)
        for cust in results:
            customers[cust.id] = cust
    return customers

def get_broker_ids(broker: Broker) -> Set:
    broker_ids = set()
    with Session(engine) as session:
        statement = select(Broker.id).where(Broker.org == broker.org)
        results = session.exec(statement)
        for id in results:
            broker_ids.add(id)
    return broker_ids

def get_brokers(broker: Broker) -> Dict:
    brokers = dict()
    with Session(engine) as session:
        statement = select(Broker).where(Broker.org == broker.org)
        results = session.exec(statement)
        for brok in results:
            brokers[brok.id] = brok
    return brokers

def add_customer(customer: Customer) -> Customer:
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
    return customer

def delete_customer(customer: Customer) -> None:
    with Session(engine) as session:
        customer = session.get(Customer, customer.id)
        session.delete(customer)
        session.commit()

def update_customer(customer: Customer) -> Customer:
    with Session(engine) as session:
        db_customer = session.get(Customer, customer.id)
        db_customer.update(customer)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
    return db_customer

def add_broker(broker: Broker) -> Broker:
    with Session(engine) as session:
        session.add(broker)
        session.commit()
        session.refresh(broker)
    return broker

def delete_broker(broker: Broker) -> None:
    with Session(engine) as session:
        broker = session.get(Broker, broker.id)
        session.delete(broker)
        session.commit()

def update_broker(broker: Broker) -> Broker:
    with Session(engine) as session:
        db_broker = session.get(Broker, broker.id)
        db_broker.update(broker)
        session.add(db_broker)
        session.commit()
        session.refresh(db_broker)
    return db_broker
