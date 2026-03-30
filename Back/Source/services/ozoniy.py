from Source.repositories.unit_repo import UnitRepository
from datetime import datetime
from Source.integrations.ozonAPI import OzonAPI
from Source.core.settings import Settings
from Source.repositories.unit_repo import UnitRepository
from Source.schemas.ozon_response import OzonResponse


class Ozonchik:

    async def get_table(self): #метод, посылающий запрос с данными в бд - если пусто в озон
        unit_repo = UnitRepository()
        all_data = await unit_repo.get_all()
        if all_data:
            return all_data
        now = datetime.now()
        month, year = now.month, now.year
        print(f"{month=}, {year=}")
        sets = Settings()
        ozon_api = OzonAPI(sets.ozon_base_url, sets.ozon_api_key, sets.ozon_client_id)
        ozon_response = await ozon_api.post(
            "v1/finance/realization/posting",
            payload={"month": month, "year": year}
        )
        order_ids = await unit_repo.insert_many_item(ozon_response)
        await unit_repo.insert_many_delivery(ozon_response, order_ids)
        await unit_repo.insert_many_return(ozon_response, order_ids)
        return ozon_response

