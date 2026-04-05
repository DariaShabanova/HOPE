from pydantic import BaseModel as BaseSchema, ConfigDict
#from Source.schemas.ozon_response import OzonRow
from datetime import date
from typing import Optional


class DataResponse(BaseSchema):
    name: str
    offer_id: str
    commission_ratio: float
    seller_price_per_instance: float
    created_date: date
    delivery_amount: float
    delivery_price_per_instance: float
    delivery_quantity: int
    delivery_total: float
    return_amount: Optional[float]
    return_price_per_instance: Optional[float]
    return_quantity: Optional[int]
    return_total: Optional[float]

    model_config = ConfigDict(from_attributes=True)


class AllDataResponse(BaseSchema):
    result: list[DataResponse]