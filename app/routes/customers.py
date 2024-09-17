from fastapi import APIRouter, Query
from fastapi import Depends, Security

from typing import Dict, List, Optional

from ..config import logger
from ..config.consts import PATH_PREFIX_CUSTOMER, CustomerRoutes, ORG

from ..models.models import Customer, ExceptionClass

from ..service import CreateCustomerService, ReadCustomerService, UpdateCustomerService, DeleteCustomerService

from ..utils import VerifyToken, CustomerValidators, set_org_model, set_org_multiple_model

apiRouter = APIRouter(prefix=PATH_PREFIX_CUSTOMER)
auth = VerifyToken()

bad_request_responses = {
    400: {
        "description": "Error: Bad Request",
        "model": ExceptionClass
    }
}

auth_responses = {
    401: {
        "description": "Error: Unauthorized",
        "model": ExceptionClass
    },
    403: {
        "description": "Error: Forbidden",
        "model": ExceptionClass
    }
}

@apiRouter.post(CustomerRoutes.POST_ADD_CUSTOMER, response_model=Customer, responses=bad_request_responses | auth_responses)
async def add_customer(customer: Customer = Depends(CustomerValidators.add_validator), auth_result: Dict = Security(auth.verify)) -> Customer:
    set_org_model(customer, auth_result)
    logger.debug("In add_customer:" + str(customer))
    return CreateCustomerService.add_customer(customer)

@apiRouter.put(CustomerRoutes.PUT_DEACTIVATE_CUSTOMERS, response_model=List[Customer], responses=auth_responses)
async def deactivate_customers(customers: List[Customer] = Depends(CustomerValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Customer]:
    set_org_multiple_model(customers, auth_result)
    logger.debug("In deactivate_customers:" + str(customers))
    UpdateCustomerService.deactivate_customers(customers)
    return await get_all_customers(auth_result)

@apiRouter.put(CustomerRoutes.PUT_RECOVER_CUSTOMERS, response_model=List[Customer], responses=auth_responses)
async def recover_customers(customers: List[Customer] = Depends(CustomerValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Customer]:
    set_org_multiple_model(customers, auth_result)
    logger.debug("In recover_customers:" + str(customers))
    UpdateCustomerService.recover_customers(customers)
    return await get_deleted_customers(auth_result)

@apiRouter.put(CustomerRoutes.PUT_CUST_ADDED_IN_TRANS, response_model=Customer, responses=bad_request_responses | auth_responses)
async def cust_added_in_trans(customer: Customer = Depends(CustomerValidators.id_validator), auth_result: Dict = Security(auth.verify)) -> Customer:
    set_org_model(customer, auth_result)
    logger.debug("In cust_added_in_trans:" + str(customer))
    return UpdateCustomerService.customer_in_transaction(customer)

@apiRouter.put(CustomerRoutes.PUT_CUST_ROLLBACK_IN_TRANS, response_model=Customer, responses=bad_request_responses | auth_responses)
async def rollback_added_in_trans(customer: Customer = Depends(CustomerValidators.rollback_validator), auth_result: Dict = Security(auth.verify)) -> Customer:
    set_org_model(customer, auth_result)
    logger.debug("In rollback_added_in_trans:" + str(customer))
    return UpdateCustomerService.customer_rollback_in_trans(customer)

@apiRouter.get(CustomerRoutes.GET_CUSTOMER + "/{customer_id}", response_model=Customer, responses=bad_request_responses | auth_responses)
async def get_customer(customer_id: int, auth_result: Dict = Security(auth.verify)) -> Customer:
    customer : Customer = Customer(id = customer_id)
    set_org_model(customer, auth_result)
    logger.debug("In get_customer:" + str(customer))
    return ReadCustomerService.get_customer(customer)

@apiRouter.get(CustomerRoutes.GET_ALL_CUSTOMERS, response_model=List[Customer], responses=auth_responses)
async def get_all_customers(auth_result: Dict = Security(auth.verify)) -> List[Customer]:
    customer : Customer = set_org_model(Customer(), auth_result)
    logger.debug("In get_all_customers:" + str(customer))
    return ReadCustomerService.get_all_customers(customer)

@apiRouter.get(CustomerRoutes.GET_CUSTOMERS_LIST+"/", response_model=List[Optional[Customer]], responses=auth_responses)
async def get_customers_list(customer_id: List[int] = Query([]), auth_result: Dict = Security(auth.verify)) -> List[Optional[Customer]]:
    logger.debug("In get_customers_list:" + str(customer_id))
    return ReadCustomerService.get_customers_list(auth_result[ORG], customer_id)

@apiRouter.get(CustomerRoutes.GET_DELETED_CUSTOMERS, response_model=List[Customer], responses=auth_responses)
async def get_deleted_customers(auth_result: Dict = Security(auth.verify)) -> List[Customer]:
    customer : Customer = set_org_model(Customer(), auth_result)
    logger.debug("In get_deleted_customers:" + str(customer))
    return ReadCustomerService.get_deleted_customers(customer)

@apiRouter.delete(CustomerRoutes.DELETE_CUSTOMERS, response_model=List[Customer], responses=auth_responses)
async def delete_customers(customers: List[Customer] = Depends(CustomerValidators.list_id_validator), auth_result: Dict = Security(auth.verify)) -> List[Customer]:
    set_org_multiple_model(customers, auth_result)
    logger.debug("In delete_customers:" + str(customers))
    DeleteCustomerService.delete_customers(customers)
    return await get_deleted_customers(auth_result)