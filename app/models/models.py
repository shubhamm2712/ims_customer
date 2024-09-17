from typing import Optional

from sqlmodel import SQLModel, Field

from pydantic import BaseModel

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org: Optional[str] = None
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None
    taxNumber: Optional[str] = None
    metaData: Optional[str] = None
    active: Optional[int] = None
    usedInTransaction: Optional[int] = None

    def update_data(self, customer: "Customer") -> None:
        self.name = customer.name
        self.address = customer.address
        self.phone = customer.phone
        self.taxNumber = customer.taxNumber
        self.metaData = customer.metaData

class ExceptionClass(BaseModel):
    detail: str