import asyncio
from api.models.asset import Asset
import asyncio
from icecream import ic
import os
from binance.client import Client
import time
from decimal import Decimal
from fastapi import Depends
from sqlalchemy.orm import Session
from api.models.base import get_db


BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")

WALLET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SYNC_PERIOD", 60))


class WalletWorker:
    def __init__(self, name, db: Session = get_db()):
        self.name = str(name)
        self.db = next(db)
        self.shutdown = False
        self.client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

    async def fetch_assets(self):
        "Fetch assets"
        while not self.shutdown:
            ic(time.time_ns())
            details = await self.client.get_account()
            non_zero_assets = [a for a in details['balances'] if float(a['free'])+float(a['locked']) > .0]
            ic(non_zero_assets)
            for a in non_zero_assets:
                asset = Asset(exchange=self.name,
                      symbol=a['asset'],
                      balance=Decimal(a['free'])+Decimal(a['locked']),
                      free=Decimal(a['free']),
                      locked=Decimal(a['locked']))
                self.db.merge(asset)
                self.db.commit()
            await asyncio.sleep(WALLET_SYNC_PERIOD)


async def main():
    ww1 = WalletWorker(1)
    asyncio.create_task(ww1.fetch_assets())


if __name__ == '__main__':
    ww = WalletWorker(1)

    loop = asyncio.get_event_loop()
    tasks = list()
    tasks.append(loop.create_task(ww.fetch_assets()))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
