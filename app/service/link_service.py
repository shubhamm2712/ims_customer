from typing import Optional

from ..config.consts import *

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer, Broker, SingleEntity

def add_link_cust_brok(customer: Customer, broker: Broker, get_customer: bool= False, get_broker: bool = False) -> Optional[SingleEntity]:
    if customer.id is None:
        customer_entity = db_ops.add_customer(customer)
    else:
        customer_entity = db_ops.get_customer(customer)
    if broker.id is None:
        broker_entity = db_ops.add_broker(broker)
    else:
        broker_entity = db_ops.get_broker(broker)
    if customer_entity.customer is None:
        raise InvalidBodyException(CUSTOMER_DOES_NOT_EXIST)
    if broker_entity.broker is None:
        raise InvalidBodyException(BROKER_DOES_NOT_EXIST)
    brokers_id = set()
    for broker in customer_entity.brokers:
        brokers_id.add(broker.id)
    if broker_entity.broker.id in brokers_id:
        raise InvalidBodyException(LINK_ALREADY_EXISTS)
    db_ops.add_customer_broker_link(customer_entity.customer, broker_entity.broker)
    if get_customer:
        return db_ops.get_customer(customer_entity.customer)
    if get_broker:
        return db_ops.get_broker(broker_entity.broker)
    return None

def del_link_cust_brok(customer: Customer, broker: Broker, get_customer: bool = False, get_broker: bool = False) -> Optional[SingleEntity]:
    customer_entity = db_ops.get_customer(customer)
    broker_entity = db_ops.get_broker(broker)
    if customer_entity.customer is None:
        raise InvalidBodyException(CUSTOMER_DOES_NOT_EXIST)
    if broker_entity.broker is None:
        raise InvalidBodyException(BROKER_DOES_NOT_EXIST)
    brokers_id = set()
    for broker in customer_entity.brokers:
        brokers_id.add(broker.id)
    if broker_entity.broker.id not in brokers_id:
        raise InvalidBodyException(LINK_DOES_NOT_EXISTS)
    db_ops.remove_customer_broker_link(customer_entity.customer, broker_entity.broker)
    if get_customer:
        return db_ops.get_customer(customer_entity.customer)
    if get_broker:
        return db_ops.get_broker(broker_entity.broker)
    return None
    
