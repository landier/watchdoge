import os
import time

from binance.client import Client

BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")

client = Client(os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET'))

print(client.get_account())

# print(client.get_asset_balance(asset='BTC'))
# print(client.get_account_status())
# print(client.get_asset_details())
# print(client.get_dust_log())
# print(client.get_asset_dividend_history())

print(client.get_sub_account_list())
