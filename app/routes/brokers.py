from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List

from ..config.consts import PATH_PREFIX_BROKER, POST_ADD_BROKER, POST_DELETE_BROKER, GET_BROKERS
from ..config.logger_config import logger

from ..models.models import Broker

from ..service import add_broker_service, del_broker_service, get_broker_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_validator, del_validator
from ..utils.utils import set_org_model

apiRouter = APIRouter(prefix=PATH_PREFIX_BROKER)
auth = VerifyToken()

# Brokers
@apiRouter.post(POST_ADD_BROKER, response_model=List[Broker])
async def add_broker(broker: Broker = Depends(add_validator), auth_result: dict = Security(auth.verify)) -> List[Broker]:
    set_org_model(broker, auth_result)
    logger.debug("In add_broker:" + str(broker))
    # add_product_service.add_product(product)
    brokers = await get_brokers(auth_result)
    return brokers

@apiRouter.post(POST_DELETE_BROKER, response_model=List[Broker])
async def delete_broker(broker: Broker = Depends(del_validator), auth_result: dict = Security(auth.verify)) -> List[Broker]:
    set_org_model(broker, auth_result)
    logger.debug("In delete_broker:" + str(broker))
    del_broker_service.del_broker(broker)
    brokers = await get_brokers(auth_result)
    return brokers

@apiRouter.get(GET_BROKERS, response_model=List[Broker])
async def get_brokers(auth_result: dict = Security(auth.verify)) -> List[Broker]:
    broker = set_org_model(Broker(), auth_result)
    logger.debug("In get_brokers:" + str(broker))
    brokers = get_broker_service.get_brokers(broker)
    return brokers
