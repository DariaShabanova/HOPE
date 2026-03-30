from pydantic import BaseModel as BaseSchema, Field
from Source.schemas.ozon_response import OzonRow


class AllDataResponse(BaseSchema):
    result: list[OzonRow]