import asyncio
import datetime
import os
import time
from decimal import Decimal

from icecream import ic
from sqlalchemy.orm import Session

from api.models.balance import Balance
from api.models.daily_balance import DailyBalance
from api.models.base import get_db


WALLET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SYNC_PERIOD", 60))
WALLET_SNAPSHOT_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SNAPSHOT_SYNC_PERIOD", 60*60*3))


class AccountWorker:
    def __init__(self, name, client, db: Session = get_db()):
        self.name = str(name)
        self.client = client
        self.db = next(db)
        self.shutdown = False

    async def fetch_balances(self):
        "Fetch assets"
        while not self.shutdown:
            ic(time.time_ns())
            details = self.client.get_account()
            # TODO: Fix bug!
            non_zero_assets = [a for a in details['balances'] if float(a['free'])+float(a['locked']) > .0]
            ic(non_zero_assets)
            for a in non_zero_assets:
                asset = Balance(exchange=self.name,
                      symbol=a['asset'],
                      balance=Decimal(a['free'])+Decimal(a['locked']),
                      free=Decimal(a['free']),
                      locked=Decimal(a['locked']))
                self.db.merge(asset)
                self.db.commit()
            await asyncio.sleep(WALLET_SYNC_PERIOD)

    async def fetch_daily_balances(self):
        "Fetch asset daily snapshot"
        while not self.shutdown:
            ic(time.time_ns())
            # ic(self.client.get_account_snapshot(type="SPOT"))
            details = self.client.get_account_snapshot(type="SPOT")
            ic(len(details['snapshotVos']))
            for daily_snapshot in details['snapshotVos']:
                update_time = daily_snapshot['updateTime']
                non_zero_assets = []
                for asset in daily_snapshot['data']['balances']:
                    if float(asset['free'])+float(asset['locked']) > .0:
                        non_zero_assets.append(asset)

                for asset in non_zero_assets:
                    day = datetime.date.fromtimestamp(update_time/1000)
                    ic(day)
                    asset_daily_snapshot = DailyBalance(exchange=self.name,
                        symbol=asset['asset'],
                        day=day,
                        snapshot_time=update_time,
                        balance=Decimal(asset['free'])+Decimal(asset['locked']),
                        free=Decimal(asset['free']),
                        locked=Decimal(asset['locked'])
                        )
                    self.db.merge(asset_daily_snapshot)
                    self.db.commit()
            await asyncio.sleep(WALLET_SNAPSHOT_SYNC_PERIOD)

    async def fetch_trades(self):
        pass
