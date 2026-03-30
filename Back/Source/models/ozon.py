from Source.models.base import BaseModel
from sqlalchemy.orm import mapped_column, Mapped  # для создания модели данных - таблицы ещё нет,
from sqlalchemy import String, ForeignKey  # для того, чтобы задать макс длину
from datetime import datetime  # тип данных даты в питоне


class ItemModel(BaseModel):  # создаём модель данных
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True)
    commission_ratio: Mapped[float] = mapped_column()
    name: Mapped[str] = mapped_column(String(511), nullable=False)
    offer_id: Mapped[int] = mapped_column(nullable=False)  # может привести к проблемам посмотрим потом если че
    seller_price_per_instance: Mapped[float] = mapped_column()
    created_date: Mapped[datetime] = mapped_column()


class DeliveryModel(BaseModel):  # создаём модель данных
    __tablename__ = "delivery_commission"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE'), nullable=False, unique=True)
    amount: Mapped[float] = mapped_column()
    price_per_instance: Mapped[float] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    total: Mapped[float] = mapped_column()


class ReturnModel(BaseModel):  # создаём модель данных
    __tablename__ = "return_commission"
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('item.id', ondelete='CASCADE'), nullable=False, unique=True)
    amount: Mapped[float] = mapped_column()
    price_per_instance: Mapped[float] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    total: Mapped[float] = mapped_column()

