import os
import time
import binance
from uuid import uuid4
from influxdb_client import Point, WritePrecision
from feeder.fetchers.base_fetcher import BaseFetcher
from feeder.conf import pairs


BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")


class BinanceFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()

    def _on_trade(self, e):
        # TODO: count collisions on trade time with suffix
        # time_suffix = str(uuid4().int)[:6]
        time_suffix = str(time.time_ns())[:6]
        trade = Point(e.event_type)\
            .tag('pair', e.symbol)\
            .field('price', float(e.price))\
            .field('quantity', float(e.quantity))\
            .time(int(str(e.trade_time) + time_suffix), WritePrecision.NS)
        self.dal.write(trade)

    def _on_agg_trade(self, e):
        # TODO: count collisions on trade time with suffix
        # time_suffix = str(uuid4().int)[:6]
        time_suffix = str(time.time_ns())[:6]
        trade = Point(e.event_type)\
            .tag('pair', e.symbol)\
            .field('price', float(e.price))\
            .field('quantity', float(e.quantity))\
            .time(int(str(e.trade_time) + time_suffix), WritePrecision.NS)
        self.dal.write(trade)

    async def run(self, loop):
        client = binance.Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        await client.load()

        # client.events.register_event(on_agg_trade, "btcusdt@aggTrade")
        for pair in pairs:
            client.events.register_event(self._on_trade, f"{pair}@trade")
        # print(client.assert_symbol_exists("BTCUSDT"))
        # client.events.register_event(on_depth, "btcusdt@depth@100ms")
        # client.events.register_event(on_partial_depth, "btcusdt@depth20@100ms")
        # client.events.register_event(on_partial_depth, "btcusdt@depth20@1000ms")
        loop.create_task(client.start_market_events_listener())
