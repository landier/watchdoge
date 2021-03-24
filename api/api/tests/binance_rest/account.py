import hmac
import hashlib
import os
import time
import requests
from urllib.parse import urlencode


API_ENDPOINT = "https://api.binance.com"
BINANCE_API_KEY=os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET=os.getenv("BINANCE_API_SECRET")
headers={"Content-Type":"application/json", "X-MBX-APIKEY": BINANCE_API_KEY}
URL_PATH = "/sapi/v1/accountSnapshot"
URL_PARAMS = {"type": "SPOT", "limit": 5}
URL = f"{API_ENDPOINT}{URL_PARAMS}"


def hashing(query_string):
    return hmac.new(BINANCE_API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()


def get_timestamp():
    return int(time.time() * 1000)


def dispatch_request(http_method):
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json;charset=utf-8',
        'X-MBX-APIKEY': BINANCE_API_KEY
    })
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')


def send_signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())

    url = API_ENDPOINT + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = dispatch_request(http_method)(**params)
    return response.json()

print(send_signed_request("GET", URL_PATH, URL_PARAMS))
print(send_signed_request("GET", "/sapi/v1/capital/config/getall"))
print(send_signed_request('GET', '/api/v3/account'))
