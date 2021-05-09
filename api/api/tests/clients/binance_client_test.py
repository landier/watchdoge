import unittest

from api.clients.binance_client import BinanceClient


class TestBinanceClient(unittest.TestCase):

    def test_instantiate_two(self):
        # Given
        client1 = BinanceClient()
        client2 = BinanceClient()
        
        # When & Then
        self.assertEqual(id(client1), id(client2))


if __name__ == '__main__':
    unittest.main()
