from ..config.consts import ID_NOT_FOUND

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Broker

def is_update(broker: Broker) -> bool:
    if broker.id:
        return True
    return False

def validate_update_broker(broker: Broker) -> None:
    brok_ids = db_ops.get_broker_ids(broker)
    if broker.id not in brok_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def add_broker(broker: Broker) -> None:
    isUpdate = is_update(broker)
    if isUpdate:
        validate_update_broker(broker)
        db_ops.update_broker(broker)
    else:
        db_ops.add_broker(broker)
