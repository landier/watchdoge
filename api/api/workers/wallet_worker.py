import asyncio
from api.models.asset import Asset
import asyncio
from icecream import ic
import binance
import os


BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")

WALLET_SYNC_PERIOD = int(os.getenv("WATCHDODGE_WALLET_SYNC_PERIOD", 60))


class WalletWorker():
    def __init__(self, name):
        self.name = name
        self.shutdown = False
    
    def start(self):
        pass

    async def fetch_assets(self):
        "Fetch assets"
        while not self.shutdown:
            ic("bim " + str(self.name))
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
