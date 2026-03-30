from fastapi import FastAPI
from Source.API.routers.index import router as index_router
from Source.API.routers.ozon import router as ozon_router

def getApp(): #создали приложение для фастапи - для увикорн
    app = FastAPI(title="UnitApi", contact={"name":"DaSha", "tg": "@d_shab_17"})
    app.include_router(index_router) #добавил путь к страниц /индекс
    app.include_router(ozon_router)
    return app

application = getApp()