import asyncio
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api import crud, schemas
from api.models import item, user
from api.models.asset import Asset
from api.models.balance import Balance
from api.models.symbol import Symbol
from api.models.ticker import Ticker
from api.models.base import Base, SessionLocal, engine, get_db
from api.workers.account_worker import AccountWorker
from api.workers.market_worker import MarketWorker
from api.clients.binance_client import BinanceClient
from api.helpers.symbol_helper import SymbolHelper
from api.helpers.seeder import load_seed_data


app = FastAPI()

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


@app.on_event("startup")
async def startup_event(client=BinanceClient()):
    if os.environ.get('ENV', 'dev') == 'dev':
        Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    
    load_seed_data()
    # exit(0)
    SymbolHelper(BinanceClient()).refresh_symbols()
    SymbolHelper(BinanceClient()).refresh_assets()

    app.account_worker = AccountWorker("Binance", client)
    app.market_worker = MarketWorker("Binance", client)
    app.tasks = [
        asyncio.create_task(app.account_worker.fetch_balances()),
        asyncio.create_task(app.account_worker.fetch_daily_balances()),
        asyncio.create_task(app.account_worker.fetch_trades()),
        asyncio.create_task(app.market_worker.fetch_markets()),
    ]


@app.on_event("shutdown")
def shutdown_event():
    [t.cancel() for t in app.tasks]
    # with open("log.txt", mode="a") as log:
    #     log.write("Application shutdown")


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/balances/", response_model=List[schemas.Balance])
def get_balances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    balances = db.query(Balance).offset(skip).limit(limit).all()
    return balances

@app.get("/assets/", response_model=List[schemas.Asset])
def get_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    assets = db.query(Asset).offset(skip).limit(limit).all()
    return assets

@app.get("/symbols/", response_model=List[schemas.Symbol])
def get_symbols(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    symbols = db.query(Symbol).offset(skip).limit(limit).all()
    return symbols

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
