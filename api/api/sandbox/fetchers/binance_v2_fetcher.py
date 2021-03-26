import asyncio
import json

from binance.client import Client
from binance.websockets import BinanceSocketManager

from feeder.fetchers.base_fetcher import BaseFetcher


dcm1 = None
loop = None

# setup async callback handler for socket messages
async def on_trade(msg):
    print("boum")
    # pair = msg['s']
    # print(f'{pair} : {msg}')

# setup an async callback for the Depth Cache
async def on_process_depth(depth_cache):
    print(f"symbol {depth_cache.symbol} updated:{depth_cache.update_time}")
    print("Top 5 asks:")
    print(len(depth_cache.get_asks()))
    # print("Top 5 bids:")
    # print(depth_cache.get_bids()[:5])

def process_m_message(msg):
    print("stream: {} data: {}".format(msg['stream'], msg['data']))


class BinanceV2Fetcher(BaseFetcher):
    def __init__(self):
        super().__init__()

    async def run(self):
        global dcm1, loop

        # initialise the client
        self.client = Client()

        # run some simple requests
        # print(json.dumps(await self.client.get_exchange_info(), indent=2))
        # print(json.dumps(await self.client.get_symbol_ticker(symbol="BTCUSDT"), indent=2))

        # initialise socket manager
        bsm = BinanceSocketManager(self.client, loop)

        conn_key = bsm.start_multiplex_socket(['bnbbtc@aggTrade'], process_m_message)
        # bsm.start_multiplex_socket(['bnbbtc@trade',
        #                             'btcusdt@trade'
        #                             'trxbtc@trade',
        #                             'ethusdt@trade'],
        #                             on_trade)

        # create listener, can use the `ethkey` value to close the socket later
        # trxkey = await bsm.start_trade_socket('TRXBTC', on_trade)
        # trxkey = await bsm.start_trade_socket('BTCUSDT', on_trade)
        # trxkey = await bsm.start_trade_socket('ETHUSDT', on_trade)

        # create the Depth Cache
        # dcm1 = await DepthCacheManager.create(self.client, loop, 'TRXBTC', on_process_depth)

        while True:
            print("doing a sleep")
            await asyncio.sleep(20, loop=loop)


