from pydantic import BaseModel
from typing import List


class PlaceOrderSuccessResponse(BaseModel):
    consumer_id: str
    order_id: str
    name: str
    sku: str
    status: str


class ConsumerSuccessResponse(BaseModel):
    status: str
    id: str
    name: str


class GetOrderSuccessResponse(BaseModel):
    status: str
    data: object


class ErrorResponse(BaseModel):
    status: str
    errors: List
