import asyncio
import os
from decimal import Decimal

from icecream import ic
from sqlalchemy.orm import Session

from api.models import Ticker
from api.models.base import get_db


MARKET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_MARKET_SYNC_PERIOD", 60))

PAIRS = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]

class MarketWorker:
    def __init__(self, exchange, client, db: Session = get_db()):
        self.exchange = str(exchange)
        self.client = client
        self.db = next(db)
        self.shutdown = False


    async def fetch_markets(self):
        "Fetch markets"
        while not self.shutdown:
            details = self.client.get_ticker()
            usd_pairs = [ticker for ticker in details if 'USD' in ticker['symbol']]
            # usd_pairs = [ticker for ticker in details if ticker['symbol'][-4:]=='USDT']
            # usd_pairs = [ticker for ticker in details if ticker['symbol'] in PAIRS]
            # ic(usd_pairs)
            new_data = [{'exchange': self.exchange,
                         'symbol': ticker["symbol"],
                         'price_change': ticker["priceChange"],
                         'price_change_percent': ticker["priceChangePercent"],
                         'weighted_avg_price': ticker["weightedAvgPrice"],
                         'prev_close_price': ticker["prevClosePrice"],
                         'last_price': ticker["lastPrice"],
                         'last_qty': ticker["lastQty"],
                         'bid_price': ticker["bidPrice"],
                         'bid_qty': ticker["bidQty"],
                         'ask_price': ticker["askPrice"],
                         'ask_qty': ticker["askQty"],
                         'open_price': ticker["openPrice"],
                         'high_price': ticker["highPrice"],
                         'low_price': ticker["lowPrice"],
                         'volume':ticker["volume"],
                         'open_time':ticker["openTime"],
                         'close_time':ticker["closeTime"],
                         'first_id': ticker["firstId"],
                         'last_id': ticker["lastId"],
                         'count': ticker["count"]
                        }
                        for ticker in usd_pairs]
            self.db.bulk_insert_mappings(Ticker, new_data)
            self.db.commit()
            await asyncio.sleep(MARKET_SYNC_PERIOD)

    async def fetch_pairs(self):
        "Fetch pairs"
        while not self.shutdown:
            response = self.client.exchange_info()
            if 'data' in response:
                response = response['data']
                ic(response)
                # pairs = []
                # for s in response['symbols']:
                #     pairs.append({
                #         s['symbol'])
                    
            # new_data = [{'exchange': self.exchange,
            #              'symbol': ticker["symbol"],
            #              'price_change': ticker["priceChange"],
            #              'price_change_percent': ticker["priceChangePercent"],
            #              'weighted_avg_price': ticker["weightedAvgPrice"],
            #              'prev_close_price': ticker["prevClosePrice"],
            #              'last_price': ticker["lastPrice"],
            #              'last_qty': ticker["lastQty"],
            #              'bid_price': ticker["bidPrice"],
            #              'bid_qty': ticker["bidQty"],
            #              'ask_price': ticker["askPrice"],
            #              'ask_qty': ticker["askQty"],
            #              'open_price': ticker["openPrice"],
            #              'high_price': ticker["highPrice"],
            #              'low_price': ticker["lowPrice"],
            #              'volume':ticker["volume"],
            #              'open_time':ticker["openTime"],
            #              'close_time':ticker["closeTime"],
            #              'first_id': ticker["firstId"],
            #              'last_id': ticker["lastId"],
            #              'count': ticker["count"]
            #             }
            #             for ticker in usd_pairs]
            # self.db.bulk_insert_mappings(Ticker, new_data)
            # self.db.commit()
            # await asyncio.sleep(MARKET_SYNC_PERIOD)
