from fastapi import APIRouter
from fastapi import Depends, Security

from typing import List

from ..config.consts import PATH_PREFIX_CUSTOMER, POST_ADD_CUSTOMER, POST_DELETE_CUSTOMER, GET_CUSTOMERS
from ..config.logger_config import logger

from ..models.models import Customer

from ..service import add_customer_service, del_customer_service, get_customer_service

from ..utils.auth_validation import VerifyToken
from ..utils.req_body_validation import add_validator, del_validator
from ..utils.utils import set_org_model

apiRouter = APIRouter(prefix=PATH_PREFIX_CUSTOMER)
auth = VerifyToken()

# Customers
@apiRouter.post(POST_ADD_CUSTOMER, response_model=List[Customer])
async def add_customer(customer: Customer = Depends(add_validator), auth_result: dict = Security(auth.verify)) -> List[Customer]:
    set_org_model(customer, auth_result)
    logger.debug("In add_customer:" + str(customer))
    add_customer_service.add_customer(customer)
    customers = await get_customers(auth_result)
    return customers

@apiRouter.post(POST_DELETE_CUSTOMER, response_model=List[Customer])
async def delete_customer(customer: Customer = Depends(del_validator), auth_result: dict = Security(auth.verify)) -> List[Customer]:
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
