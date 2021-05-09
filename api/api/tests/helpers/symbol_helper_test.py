import unittest

from api.clients.binance_client import BinanceClient
from api.helpers.symbol_helper import SymbolHelper


class TestSymbolHelper(unittest.TestCase):

    def test_fetch_symbols(self):
        # Given
        client = BinanceClient()
        helper = SymbolHelper(client)
        
        # When
        helper.fetch_symbols()

        # Then
        print(helper.all_symbols)
        self.assertGreater(len(helper.all_symbols), 0)
        self.assertGreater(len(helper.usd_symbols), 0)

    def test_load_assets(self):
        # Given
        client = BinanceClient()
        helper = SymbolHelper(client)
        
        # When
        helper.load_assets()

        # Then
        self.assertGreater(len(helper.all_assets), 0)
        # self.assertGreater(len(helper.usd_symbols), 0)


if __name__ == '__main__':
    unittest.main()
