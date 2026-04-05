from datetime import datetime
from Source.integrations.ozonAPI import OzonAPI
from Source.core.settings import Settings
from Source.repositories.unit_repo import UnitRepository
from Source.utils import find_last_date
from Source.schemas.response import AllDataResponse, DataResponse
import json


class Ozonchik:

    async def get_table(self): #метод, посылающий запрос с данными в бд - если пусто в озон
        unit_repo = UnitRepository()
        now = datetime.now()
        all_data = await unit_repo.get_all()
        if all_data:
            return AllDataResponse(result=all_data)
        sets = Settings()
        ozon_api = OzonAPI(sets.ozon_base_url, sets.ozon_api_key, sets.ozon_client_id)
        ozon_response = await ozon_api.post(
            "v1/finance/realization/posting",
            payload=json.dumps(find_last_date(now.month, now.year))
        )
        order_ids = await unit_repo.insert_many_item(ozon_response)
        await unit_repo.insert_many_delivery(ozon_response, order_ids)
        await unit_repo.insert_many_return(ozon_response, order_ids)
        await unit_repo.session.commit()
        data_response = [
            DataResponse(
                name=data.item.name,
                offer_id=data.item.offer_id,
                commission_ratio=data.commission_ratio,
                seller_price_per_instance=data.seller_price_per_instance,
                created_date=data.order.created_date,
                delivery_amount=data.delivery_commission.amount,
                delivery_price_per_instance=data.delivery_commission.price_per_instance,
                delivery_quantity=data.delivery_commission.quantity,
                delivery_total=data.delivery_commission.total,
                return_amount=data.return_commission.amount,
                return_price_per_instance=data.return_commission.price_per_instance,
                return_quantity=data.return_commission.quantity,
                return_total=data.return_commission.total,
            )
            for data in ozon_response
        ]
        return AllDataResponse(result=data_response)

