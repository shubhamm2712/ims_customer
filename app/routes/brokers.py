from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List, Optional

from ..config.consts import PATH_PREFIX_BROKER, POST_ADD_BROKER, POST_DELETE_BROKER, GET_BROKERS, GET_BROKER
from ..config.logger_config import logger

from ..models.models import Customer, Broker, SingleEntity

from ..service import add_broker_service, del_broker_service, get_broker_service, link_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_valid_broker, valid_broker, add_link_customer_validator, add_link_broker_validator, del_link_customer_validator, del_link_broker_validator
from ..utils.utils import set_org_model

apiRouter = APIRouter(prefix=PATH_PREFIX_BROKER)
auth = VerifyToken()

# Brokers
@apiRouter.post(POST_ADD_BROKER, response_model=SingleEntity)
async def add_broker(broker: Broker = Depends(add_valid_broker), auth_result: dict = Security(auth.verify)) -> SingleEntity:
    set_org_model(broker, auth_result)
    logger.debug("In add_broker:" + str(broker))
    broker_entity = add_broker_service.add_broker(broker)
    return broker_entity

@apiRouter.post(POST_DELETE_BROKER, response_model=List[Broker])
async def delete_broker(broker: Broker = Depends(valid_broker), auth_result: dict = Security(auth.verify)) -> List[Broker]:
    set_org_model(broker, auth_result)
    logger.debug("In delete_broker:" + str(broker))
    del_broker_service.del_broker(broker)
    brokers = await get_brokers(auth_result)
    return brokers

@apiRouter.get(GET_BROKERS, response_model=List[Broker])
async def get_brokers(auth_result: dict = Security(auth.verify)) -> List[Broker]:
    broker = set_org_model(Broker(), auth_result)
    logger.debug("In get_brokers: " + str(broker))
    brokers = get_broker_service.get_brokers(broker)
    return brokers

@apiRouter.get(GET_BROKER, response_model=Optional[SingleEntity])
async def get_broker(broker: Broker = Depends(valid_broker), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(broker, auth_result)
    logger.debug("In get_broker: " + str(broker))
    broker_entity = get_broker_service.get_broker(broker)
    return broker_entity

# Link Broker
@apiRouter.post("/add_link", response_model=Optional[SingleEntity])
async def add_link(customer: Customer = Depends(add_link_customer_validator), broker: Broker = Depends(add_link_broker_validator), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(customer, auth_result)
    set_org_model(broker, auth_result)
    logger.debug("In add_link Customer:" + str(customer) + " Broker: " + str(broker))
    return link_service.add_link_cust_brok(customer, broker, get_broker=True)

@apiRouter.post("/del_link", response_model=Optional[SingleEntity])
async def del_link(customer: Customer = Depends(del_link_customer_validator), broker: Broker = Depends(del_link_broker_validator), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(customer, auth_result)
    set_org_model(broker, auth_result)
    logger.debug("In del_link Customer:" + str(customer) + " Broker: " + str(broker))
    return link_service.del_link_cust_brok(customer, broker, get_broker=True)