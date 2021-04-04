import asyncio
from api.models.asset import Asset
import asyncio
from icecream import ic

WALLET_WORKER_PERIOD_IN_S = 60


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
            await asyncio.sleep(1)

async def main():
    ww1 = WalletWorker(1)
    asyncio.create_task(ww1.fetch_assets())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # asyncio.run(main())
    loop.run_until_complete(main)
    
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(
