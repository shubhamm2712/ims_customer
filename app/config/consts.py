## Routes
PATH_PREFIX_CUSTOMER = "/customers"
PATH_PREFIX_BROKER = "/brokers"
POST_ADD_CUSTOMER = "/add_customer"
POST_DELETE_CUSTOMER = "/del_customer"
GET_CUSTOMERS = "/get_customers"
POST_ADD_BROKER = "/add_broker"
POST_DELETE_BROKER = "/del_broker"
GET_BROKERS = "/get_brokers"

# Config file
CONFIG_FILE = ".env"

# Logger
LOG_FILE = "app/app.log"

# Databases
DB_FILE_NAME = "app/database/database.db"
DB_ECHO = True

# Service
FLOATING_POINT_ERROR = 10e-4

# EXCEPTIONS
ORG_NOT_FOUND = "Org not found"
ID_NOT_FOUND = "ID not found"
NAME_NOT_FOUND = "Name not found"
INVALID_PRODUCT_DETAILS_TYPE = "Invalid product details type"

# MODEL
ORG = "org"