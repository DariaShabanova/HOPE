from pydantic import BaseModel as BaseSchema, Field, field_validator
from datetime import date
from Source.utils import date_correct
from typing import Optional


class OzonCommission(BaseSchema):
    amount: float = Field(description="Сумма.")
    price_per_instance: float = Field(description="Цена за экземпляр.")
    quantity: float = Field(description="Количество товара.")
    total: float = Field(description="Итого к начислению.")


class OzonItem(BaseSchema):
    name: str = Field(description="Наименование товара.")
    offer_id: str = Field(description="Идентификатор товара в cистеме продавца — артикул.")


class OzonOrder(BaseSchema):
    created_date: date = Field(description="Дата заказа в формате «ГГГГ-ММ-ДД».")

    @field_validator("created_date", mode="before")
    @classmethod
    def checked(cls, value: str):
        v: date = date.fromisoformat(date_correct(value))
        return v




class OzonRow(BaseSchema):
    commission_ratio: float = Field(description="Доля комиссии за продажу по категории")
    delivery_commission: OzonCommission
    item: OzonItem
    return_commission: Optional[OzonCommission] = Field(None)
    seller_price_per_instance: float = Field(description="Цена продавца с учётом скидки.")
    order: OzonOrder


class OzonResponse(BaseSchema):
    rows: list[OzonRow]

