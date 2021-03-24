from binance.websockets import BinanceSocketManager
from binance.client import Client

from sqlalchemy.orm import Session
from schemas import Trade

api_key = "sJci16AphYw2TqyjcJdMhHo6DH5873PYTPRcfHbvLv8Dqq9q0LdXsMeq2i6xklKm"
api_secret = "A2SsIg8AsKthhJvP2sm8ct9JXqM5l2C2iqbHi6JUNKgmpubNx9y9rxqoZLdUK5mI"

client = Client(api_key, api_secret)
bm = BinanceSocketManager(client, user_timeout=60)

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    Trade()
    # do something

# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BTCUSDT', process_message)
# then start the socket manager
bm.start()
