import asyncio
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api import crud, schemas
from api.models import item, user
from api.models.asset import Asset
from api.models.base import Base, SessionLocal, engine, get_db
from api.workers.wallet_worker import WalletWorker
from api.workers.market_worker import MarketWorker

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    app.wallet_worker = WalletWorker("Binance")
    app.market_worker = MarketWorker("Binance")
    app.tasks = [
        asyncio.create_task(app.wallet_worker.fetch_asset_balances()),
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


@app.get("/assets/", response_model=List[schemas.Asset])
def get_assets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    assets = db.query(Asset).offset(skip).limit(limit).all()
    return assets


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


# asset = Asset(exchange="Binance",
#                       symbol="test",
#                       balance=1.,locked=1., free=1.)
# db = next(get_db())
# db.add(asset)
# db.commit()
