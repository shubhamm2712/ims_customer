## Routes
PATH_PREFIX_CUSTOMER = "/customers"

# Customer Routes
class CustomerRoutes:
    POST_ADD_CUSTOMER = "/add_customer"
    
    PUT_DEACTIVATE_CUSTOMERS = "/deactivate_customers"
    PUT_RECOVER_CUSTOMERS = "/recover_customers"
    PUT_CUST_ADDED_IN_TRANS = "/customer_add_in_transaction"
    PUT_CUST_ROLLBACK_IN_TRANS = "/customer_rollback_in_transaction"

    GET_ALL_CUSTOMERS = "/get_all_customers"
    GET_CUSTOMER = "/get_customer"
    GET_CUSTOMERS_LIST = "/get_customers_list"
    GET_DELETED_CUSTOMERS = "/get_deleted_customers"

    DELETE_CUSTOMERS = "/delete_customers"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_ECHO = False
DB_NAME = "imscustomer"

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "ID not found"
ACTIVE_ID_NOT_FOUND = "Active ID not found"
NAME_NOT_FOUND = "Name not found"
USED_IN_TRANSACTION_NOT_FOUND = "usedInTransaction not found"
INVALID_CUSTOMER_DETAILS_TYPE = "Invalid customer details type"
CUSTOMER_DETAILS_MISSING = "Customer details are missing"
CUSTOMER_DOES_NOT_EXIST = "Customer does not exist"
CANNOT_BE_USED_IN_TRANSACTION = "Cannot be used in transaction"
CANNOT_BE_ROLLBACKED_IN_TRANSACTION = "Cannot be rolled back in transaction"

# MODEL
ORG = "org"