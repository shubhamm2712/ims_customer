from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

class CustomerBroker(SQLModel, table=True):
    customerId: Optional[int] = Field(default=None, foreign_key="customer.id", primary_key=True)
    brokerId: Optional[int] = Field(default=None, foreign_key="broker.id", primary_key=True)

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    taxNumber: Optional[str] = None

    brokers: list["Broker"] = Relationship(back_populates="customers", link_model=CustomerBroker)

    def update(self, customer: "Customer"):
        self.id = customer.id
        self.org = customer.org
        self.name = customer.name
        self.address = customer.address
        self.phone = customer.phone
        self.taxNumber = customer.taxNumber

class Broker(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None

    customers: list["Customer"] = Relationship(back_populates="brokers", link_model=CustomerBroker)

    def update(self, broker: "Broker"):
        self.id = broker.id
        self.org = broker.org
        self.name = broker.name
        self.phone = broker.phone

class SingleEntity(SQLModel):
    customer: Optional[Customer] = None
    broker: Optional[Broker] = None
    customers: List[Customer] = []
    brokers: List[Broker] = []