import asyncio
from datetime import datetime
import os
import time
from decimal import Decimal

from icecream import ic
from sqlalchemy.orm import Session

from api.models.balance import Balance
from api.models.trade import Trade
from api.models.symbol import Symbol
from api.models.daily_balance import DailyBalance
from api.models.base import get_db


WALLET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SYNC_PERIOD", 60))
WALLET_SNAPSHOT_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SNAPSHOT_SYNC_PERIOD", 60*60*3))
TRADES_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SNAPSHOT_SYNC_PERIOD", 60*60*3))


class AccountWorker:
    def __init__(self, name, client, db: Session = get_db()):
        self.name = str(name)
        self.client = client
        self.db = next(db)
        self.shutdown = False

    async def fetch_balances(self):
        "Fetch assets"
        while not self.shutdown:
            details = self.client.get_account()
            # TODO: Fix bug!
            non_zero_assets = [a for a in details['balances'] if float(a['free'])+float(a['locked']) > .0]
            for a in non_zero_assets:
                asset = Balance(exchange=self.name,
                      asset=a['asset'],
                      balance=Decimal(a['free'])+Decimal(a['locked']),
                      free=Decimal(a['free']),
                      locked=Decimal(a['locked']))
                self.db.merge(asset)
                self.db.commit()
            await asyncio.sleep(WALLET_SYNC_PERIOD)

    async def fetch_daily_balances(self):
        "Fetch asset daily snapshot"
        while not self.shutdown:
            details = self.client.get_account_snapshot(type="SPOT")
            for daily_snapshot in details['snapshotVos']:
                update_time = daily_snapshot['updateTime']
                non_zero_assets = []
                for asset in daily_snapshot['data']['balances']:
                    if float(asset['free'])+float(asset['locked']) > .0:
                        non_zero_assets.append(asset)

                for asset in non_zero_assets:
                    day = datetime.date.fromtimestamp(update_time/1000)
                    asset_daily_snapshot = DailyBalance(exchange=self.name,
                        asset=asset['asset'],
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
        """
        Fetch user trades
        """
        while not self.shutdown:
            for symbol, in self.db.query(Symbol.symbol).order_by(Symbol.symbol):
<<<<<<< HEAD
                trades = self.client.get_my_trades(symbol=symbol)
                for t in trades:
=======
                ic(symbol)
                trades = self.client.get_my_trades(symbol=symbol)
                for t in trades:
                    ic(t)
                    # ic(datetime.datetime(t['time']/1000))
>>>>>>> f7697e7 (WIP - Add fetch trades)
                    trade = Trade(exchange=self.name,
                        symbol=t['symbol'],
                        trade_id=t['id'],
                        order_id=t['orderId'],
                        order_list_id=t['orderListId'],
                        price=Decimal(t['price']),
                        quantity=Decimal(t['qty']),
                        quote_quantity=Decimal(t['quoteQty']),
<<<<<<< HEAD
                        commission=Decimal(t['commission']),
                        commission_asset=t['commissionAsset'],
                        traded_at=datetime.fromtimestamp(int(t['time']/1000)),
=======
                        # commission=Decimal(t['commission']),
                        # commission_asset=Decimal(t['commissionAsset']),
                        # trade_at=datetime.datetime(t['time']/1000),
                        # datetime.date.fromtimestamp(update_time/1000)
>>>>>>> f7697e7 (WIP - Add fetch trades)
                        is_buyer=t['isBuyer'],
                        is_maker=t['isMaker'],
                        is_best_match=t['isBestMatch'],
                        )
<<<<<<< HEAD
                    self.db.merge(trade)
                self.db.commit()
            await asyncio.sleep(TRADES_SYNC_PERIOD) 
=======
                    ic(trade)
                    self.db.merge(trade)
                self.db.commit()
            await asyncio.sleep(TRADES_SYNC_PERIOD) 

    # 'symbol': 'BCHBUSD',
    # 'id': 6629335,
    # 'orderId': 239005272,
    # 'orderListId': -1,
    # 'price': '960.00000000',
    # 'qty': '0.25064000',
    # 'quoteQty': '240.61440000',
    # 'commission': '0.00000000',
    # 'commissionAsset': 'BNB',
    # 'time': 1618825932410,
    # 'isBuyer': True,
    # 'isMaker': True,
    # 'isBestMatch': True
>>>>>>> f7697e7 (WIP - Add fetch trades)
