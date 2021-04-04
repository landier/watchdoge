import asyncio
import os
import time
from decimal import Decimal

from binance.client import Client
from fastapi import Depends
from icecream import ic
from sqlalchemy.orm import Session

from api.models.asset import Asset
from api.models.base import get_db

BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")

MARKET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_MARKET_SYNC_PERIOD", 60))


class MarketWorker:
    def __init__(self, name, db: Session = get_db()):
        self.name = str(name)
        self.db = next(db)
        self.shutdown = False
        self.client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

    async def fetch_markets(self):
        "Fetch markets"
        while not self.shutdown:
            ic(time.time_ns())
            details = await self.client.get_ticker()
            ic(details)
            # non_zero_assets = [a for a in details['balances'] if float(a['free'])+float(a['locked']) > .0]
            # ic(non_zero_assets)
            # for a in non_zero_assets:
            #     asset = Asset(exchange=self.name,
            #           symbol=a['asset'],
            #           balance=Decimal(a['free'])+Decimal(a['locked']),
            #           free=Decimal(a['free']),
            #           locked=Decimal(a['locked']))
            #     self.db.merge(asset)
            #     self.db.commit()
            await asyncio.sleep(MARKET_SYNC_PERIOD)
