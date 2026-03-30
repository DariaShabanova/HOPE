from typing import Sequence
from Source.utils import unite
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from Source.core.settings import Settings
from Source.models.ozon import ItemModel, DeliveryModel, ReturnModel
from sqlalchemy import select, insert
from sqlalchemy.orm import aliased
from Source.schemas.ozon_response import OzonRow


def mix_item(datas: list[OzonRow]) -> list[dict]:
    result = []
    for data in datas:
        prom = {"commission_ratio": data.commission_ratio, "seller_price_per_instance": data.seller_price_per_instance,
                "created_date": data.order.created_date}
        result.append(prom | data.item.model_dump())
    return result


class UnitRepository:  # класс для работы с бд (отправки запросов в бд)
    session: AsyncSession

    def __init__(self):  # конструктор
        app_settings = Settings()  # подтянули настройки
        engine = create_async_engine(app_settings.GetURL(), pool_pre_ping=True)  # передали адрес бд
        sessionMaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession,
                                          autoflush=False)  # создаём сессию для связи с бд
        self.session = sessionMaker()  # создали сессию

    async def get_all(self):
        i = aliased(ItemModel)
        d = aliased(DeliveryModel)
        r = aliased(ReturnModel)
        query = select(
            i.name, i.offer_id, i.commission_ratio, i.seller_price_per_instance, i.created_date,
            d.amount.label("deliv_amount"), d.price_per_instance.label("deliv_price"),
            d.quantity.label("deliv_quantity"), d.total.label("deliv_total"),
            r.amount.label("return_amount"), r.price_per_instance.label("return_price"),
            r.quantity.label("return_quantity"), r.total.label("return_total")
        ).select_from(i)
        query = query.join(d, i.id == d.order_id)
        query = query.join(r, i.id == r.order_id)
        result = await self.session.execute(query)  # tекстовое выполнение запроса
        return result.scalars().all()  # получим последовательность строчек в бд

    async def insert_many_item(self, datas: list[OzonRow]) -> Sequence:
        datus = mix_item(datas)
        query = insert(ItemModel).values(datus).returning(ItemModel.id)
        result = await self.session.execute(query)
        return result.all()  # tекстовое выполнение запроса

    async def insert_many_delivery(self, datas: list[OzonRow], order_ids: list[int]):
        datus = unite([data.delivery_commission.model_dump() for data in datas], order_ids)
        query = insert(DeliveryModel).values(datus)
        await self.session.execute(query)  # tекстовое выполнение запроса
        return

    async def insert_many_return(self, datas: list[OzonRow], order_ids: list[int]):
        datus = unite([data.return_commission.model_dump() for data in datas], order_ids)
        query = insert(ReturnModel).values(datus)
        await self.session.execute(query)  # tекстовое выполнение запроса
        return
