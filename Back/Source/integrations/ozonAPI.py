from Source.integrations.abstract import ExternalAPI
from httpx import AsyncClient
from Source.schemas.ozon_response import OzonResponse, OzonRow
import json



class OzonAPI(ExternalAPI):
    async def get(self, path: str):
        async with AsyncClient(headers=self.get_headers()) as client: #контекстный менеджер
            return await client.get(self.base_url + path)

    async def post(self, path: str, payload) -> list[OzonRow]:
        async with AsyncClient(headers=self.get_headers()) as client:
            response = await client.post(self.base_url + path, data=payload)
        response_dict: dict = json.load(response)
        is_ok = response_dict.get('code', None) is None
        print(f"Response is {'OK' if is_ok else 'not OK'}")
        if not is_ok:
            print(f'Response content: {response_dict}')
            raise Exception("OzonAPI bad request")
        validated_response: OzonResponse = OzonResponse.model_validate(response_dict)
        return list(validated_response.rows)

