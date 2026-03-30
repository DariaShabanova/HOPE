import os #для того, чтобы подтянуть путь до файла переменных окружения
from pydantic_settings import BaseSettings, SettingsConfigDict  #для создания класса настроек

class Settings(BaseSettings):  #класс настроек пока бд
    db_host : str = "localhost"
    db_port : int = 5432
    db_name : str = "MakeAWish"
    db_username : str = "postgres"
    db_password : str = "1357986420"


    ozon_api_key : str = "api-key"
    ozon_client_id : str = "ask for shag"
    ozon_base_url : str = "https://ozon.ru/"



    model_config = SettingsConfigDict(env_file=os.getenv("ENV_FILE", ".env"))  #для того чтоб найти файл блин
    def GetURL(self):  #получаем адрес бд
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
