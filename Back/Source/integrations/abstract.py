from abc import ABC, abstractmethod


class ExternalAPI(ABC):
    base_url: str
    __api_key: str
    __client_id: str

    def __init__(self, base_url: str, api_key: str, client_id: str):
        self.base_url = base_url
        self.__api_key = api_key
        self.__client_id = client_id

    def get_headers(self) -> dict:
        return {"Api-Key": self.__api_key, "Client-Id": self.__client_id}


    @abstractmethod
    def get(self, path: str):
        pass

    @abstractmethod
    def post(self, path: str, payload: dict):
        pass

