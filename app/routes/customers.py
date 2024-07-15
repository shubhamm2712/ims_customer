from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List, Optional

from ..config.consts import PATH_PREFIX_CUSTOMER, POST_ADD_CUSTOMER, POST_DELETE_CUSTOMER, GET_CUSTOMERS, GET_CUSTOMER
from ..config.logger_config import logger

from ..models.models import Customer, Broker, SingleEntity

from ..service import add_customer_service, del_customer_service, get_customer_service, link_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_valid_customer, valid_customer, add_link_broker_validator, add_link_customer_validator, del_link_broker_validator, del_link_customer_validator
from ..utils.utils import set_org_model

apiRouter = APIRouter(prefix=PATH_PREFIX_CUSTOMER)
auth = VerifyToken()

# Customers
@apiRouter.post(POST_ADD_CUSTOMER, response_model=SingleEntity)
async def add_customer(customer: Customer = Depends(add_valid_customer), auth_result: dict = Security(auth.verify)) -> SingleEntity:
    set_org_model(customer, auth_result)
    logger.debug("In add_customer:" + str(customer))
    customer_entity = add_customer_service.add_customer(customer)
    return customer_entity

@apiRouter.post(POST_DELETE_CUSTOMER, response_model=List[Customer])
async def delete_customer(customer: Customer = Depends(valid_customer), auth_result: dict = Security(auth.verify)) -> List[Customer]:
    set_org_model(customer, auth_result)
    logger.debug("In delete_customer:" + str(customer))
    del_customer_service.del_customer(customer)
    customers = await get_customers(auth_result)
    return customers

@apiRouter.get(GET_CUSTOMERS, response_model=List[Customer])
async def get_customers(auth_result: dict = Security(auth.verify)) -> List[Customer]:
    customer = set_org_model(Customer(), auth_result)
    logger.debug("In get_customers:" + str(customer))
    customers = get_customer_service.get_customers(customer)
    return customers

@apiRouter.get(GET_CUSTOMER, response_model=Optional[SingleEntity])
async def get_customer(customer: Customer = Depends(valid_customer), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(customer, auth_result)
    logger.debug("In get_customer: " + str(customer))
    customer_entity = get_customer_service.get_customer(customer)
    return customer_entity

# Link Broker
@apiRouter.post("/add_link", response_model=Optional[SingleEntity])
async def add_link(customer: Customer = Depends(add_link_customer_validator), broker: Broker = Depends(add_link_broker_validator), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(customer, auth_result)
    set_org_model(broker, auth_result)
    logger.debug("In add_link Customer:" + str(customer) + " Broker: " + str(broker))
    return link_service.add_link_cust_brok(customer, broker, get_customer=True)

@apiRouter.post("/del_link", response_model=Optional[SingleEntity])
async def del_link(customer: Customer = Depends(del_link_customer_validator), broker: Broker = Depends(del_link_broker_validator), auth_result: dict = Security(auth.verify)) -> Optional[SingleEntity]:
    set_org_model(customer, auth_result)
    set_org_model(broker, auth_result)
    logger.debug("In del_link Customer:" + str(customer) + " Broker: " + str(broker))
    return link_service.del_link_cust_brok(customer, broker, get_customer=True)
