import os

from binance.client import Client


BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")


class BinanceClient:
    _client = None
    
    def __new__(self):
        if self._client is None:
            self._client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
        return self._client
    
    def __getattr__(self, attribute_name):
        return getattr(self._client, attribute_name)
    
    def __setattr__(self, attribute_name):
        return setattr(self.instance, attribute_name)
