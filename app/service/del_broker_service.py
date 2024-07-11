from ..config.consts import ID_NOT_FOUND

from ..database import db_ops

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Broker

def validate_brok_id_db(broker: Broker) -> None:
    broker_ids = db_ops.get_broker_ids(broker)
    if broker.id not in broker_ids:
        raise InvalidBodyException(ID_NOT_FOUND)

def del_broker(broker: Broker) -> None:
    validate_brok_id_db(broker)
    db_ops.delete_broker(broker)
    