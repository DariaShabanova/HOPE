from fastapi import APIRouter, status
from Source.services.ozoniy import Ozonchik
from Source.schemas.response import AllDataResponse

router = APIRouter(prefix="/ozon")


@router.get(status_code=status.HTTP_200_OK, path="/table")
async def GetTable() -> AllDataResponse:
    ozon_service = Ozonchik()
    return await ozon_service.get_table()
