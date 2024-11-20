from pydantic import BaseModel
from typing import List

"""
Create consumer request classes 
"""
class ConsumerAddress(BaseModel):
    line1: str
    city: str
    state_code: str
    zipcode: str
    primary: bool

class ConsumerName(BaseModel):
    first_name: str
    last_name: str

class ConsumerAttributes(BaseModel):
    ssn: str
    date_of_birth: str
    name: ConsumerName
    addresses: List[ConsumerAddress]

class ConsumerFields(BaseModel):
    type: str
    attributes: ConsumerAttributes

class CreateConsumerRequest(BaseModel):
    data: ConsumerFields

"""
Auth request class
"""
class AuthRequest(BaseModel):
    client_id: str
    client_secret: str
    audience: str
    scope: str
    grant_type: str

"""
Create order request classes
"""
class OrderAttributes(BaseModel):
    consumer_id: str
    portfolio_id: str
    sku: str

class OrderFields(BaseModel):
    type: str
    attributes: OrderAttributes

class CreateOrderRequest(BaseModel):
    data: OrderFields

