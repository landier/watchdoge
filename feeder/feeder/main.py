import asyncio

from feeder.fetchers.binance_fetcher import BinanceFetcher


def on_partial_depth(e):
    print(e)
    print(f"{e.last_update_id} {e.bids} {e.asks}")

def on_depth(e):
    print(e)
    print(f"{e.event_type} {e.event_time} {e.symbol} {e.first_update_id} {e.final_update_id} {e.bids} {e.asks}")


if __name__ == '__main__':
    feeder = BinanceFetcher()
    loop = asyncio.get_event_loop()
    loop.create_task(feeder.run(loop))
    loop.run_forever()
