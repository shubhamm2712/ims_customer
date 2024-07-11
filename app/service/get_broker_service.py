from typing import List

from ..database import db_ops

from ..models.models import Broker

def get_brokers(broker: Broker) -> List[Broker]:
    brokers = db_ops.get_brokers(broker)
    return list(brokers.values())