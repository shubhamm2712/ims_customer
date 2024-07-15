from typing import List, Optional

from ..config.consts import BROKER_DOES_NOT_EXIST

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Broker, SingleEntity

def get_brokers(broker: Broker) -> List[Broker]:
    brokers = db_ops.get_brokers(broker)
    return list(brokers.values())

def get_broker(broker: Broker) -> Optional[SingleEntity]:
    broker_entity = db_ops.get_broker(broker)
    if broker_entity.broker is None:
        raise InvalidBodyException(BROKER_DOES_NOT_EXIST)
    return broker_entity