from ..config.consts import ID_NOT_FOUND

from ..exceptions.invalid_body_exceptions import InvalidBodyException

from ..models.models import Customer

def del_customer(customer: Customer) -> None:
    if customer.id:
        raise InvalidBodyException(ID_NOT_FOUND)
    # delete