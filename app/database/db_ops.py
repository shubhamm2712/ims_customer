from sqlmodel import Session, select
from typing import Set, Dict, List

from .db_config import engine

from ..models.models import Customer, Broker, SingleEntity

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

def get_customer(customer: Customer) -> SingleEntity:
    customer_entity = SingleEntity()
    with Session(engine) as session:
        statement = select(Customer).where(Customer.org == customer.org, Customer.id == customer.id)
        results = session.exec(statement)
        customer = results.first()
        if customer is not None:
            customer_entity.customer = customer
            customer_entity.brokers = customer.brokers
    return customer_entity

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

def get_broker(broker: Broker) -> SingleEntity:
    broker_entity = SingleEntity()
    with Session(engine) as session:
        statement = select(Broker).where(Broker.org == broker.org, Broker.id == broker.id)
        results = session.exec(statement)
        broker = results.first()
        if broker is not None:
            broker_entity.broker = broker
            broker_entity.customers = broker.customers
    return broker_entity

def add_customer(customer: Customer) -> SingleEntity:
    customer_entity = SingleEntity()
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        customer_entity.customer = customer
        customer_entity.brokers = customer.brokers
    return customer_entity

def delete_customer(customer: Customer) -> None:
    with Session(engine) as session:
        customer = session.get(Customer, customer.id)
        session.delete(customer)
        session.commit()

def update_customer(customer: Customer) -> SingleEntity:
    customer_entity = SingleEntity()
    with Session(engine) as session:
        db_customer = session.get(Customer, customer.id)
        db_customer.update(customer)
        session.add(db_customer)
        session.commit()
        session.refresh(db_customer)
        customer_entity.customer = db_customer
        customer_entity.brokers = db_customer.brokers
    return customer_entity

def add_broker(broker: Broker) -> SingleEntity:
    broker_entity = SingleEntity()
    with Session(engine) as session:
        session.add(broker)
        session.commit()
        session.refresh(broker)
        broker_entity.broker = broker
        broker_entity.customers = broker.customers
    return broker_entity

def delete_broker(broker: Broker) -> None:
    with Session(engine) as session:
        broker = session.get(Broker, broker.id)
        session.delete(broker)
        session.commit()

def update_broker(broker: Broker) -> SingleEntity:
    broker_entity = SingleEntity()
    with Session(engine) as session:
        db_broker = session.get(Broker, broker.id)
        db_broker.update(broker)
        session.add(db_broker)
        session.commit()
        session.refresh(db_broker)
        broker_entity.broker = db_broker
        broker_entity.customers = db_broker.customers
    return broker_entity

def add_customer_broker_link(customer: Customer, broker: Broker) -> None:
    with Session(engine) as session:
        customer = session.get(Customer, customer.id)
        broker = session.get(Broker, broker.id)
        customer.brokers.append(broker)
        session.add(customer)
        session.commit()

def remove_customer_broker_link(customer: Customer, broker: Broker) -> None:
    with Session(engine) as session:
        customer = session.get(Customer, customer.id)
        broker = session.get(Broker, broker.id)
        customer.brokers.remove(broker)
        session.add(customer)
        session.commit()
