from pydantic import BaseModel as BaseSchema, Field
from datetime import datetime


class OzonCommission(BaseSchema):
    amount: float = Field(description="Сумма.")
    price_per_instance: float = Field(description="Цена за экземпляр.")
    quantity: float = Field(description="Количество товара.")
    total: float = Field(description="Итого к начислению.")


class OzonItem(BaseSchema):
    name: str = Field(description="Наименование товара.")
    offer_id: str = Field(description="Идентификатор товара в cистеме продавца — артикул.")


class OzonOrder(BaseSchema):
    created_date: datetime = Field(description="Дата заказа в формате «ГГГГ-ММ-ДД».")


class OzonRow(BaseSchema):
    commission_ratio: float = Field(description="Доля комиссии за продажу по категории")
    delivery_commission: OzonCommission
    item: OzonItem
    return_commission: OzonCommission
    seller_price_per_instance: float = Field(description="Цена продавца с учётом скидки.")
    order: OzonOrder


class OzonResponse(BaseSchema):
    rows: list[OzonRow]

