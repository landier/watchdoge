from api.models.asset import Asset
from api.models.symbol import Symbol
from api.models.base import get_db


class SymbolHelper:
    def __init__(self, client):
        self.client = client
        self.db = next(get_db())
        self._all_symbols = {}
        self._usd_symbols = {}
        self._all_assets = {}

    @property
    def all_assets(self):
        return self._all_assets
    
    @property
    def all_symbols(self):
        return self._all_symbols

    @property
    def usd_symbols(self):
        return self._usd_symbols

    def refresh_assets(self):
        self.fetch_assets()
        self.save_assets()
    
    def fetch_assets(self):
        """
        Fetch traded assets from exchange
        """
        response = self.client.get_asset_details()
        if len(response) > 0:
            self._all_assets = response

    def save_assets(self):
        print(self.all_assets)
        for asset_key, asset_details in self.all_assets.items():
            asset = Asset(
                exchange='Binance',
                asset=asset_key,
                withdraw_fee=asset_details["withdrawFee"],
                min_withdraw_amount=asset_details["minWithdrawAmount"],
                withdraw_status=asset_details["withdrawStatus"],
                deposit_status=asset_details["depositStatus"])
            self.db.merge(asset)
        self.db.commit()

    def refresh_symbols(self):
        self.fetch_symbols()
        self.save_symbols()

    def fetch_symbols(self):
        """
        Fetch traded symbols from exchange
        """
        response = self.client.get_exchange_info()
        all_symbols = {}
        usd_symbols = {}
        if 'symbols' in response:
            for s in response['symbols']:
                all_symbols[s['symbol']] = s
                if 'USD' in s['symbol']:
                    usd_symbols[s['symbol']] = s
            self._all_symbols = all_symbols
            self._usd_symbols = usd_symbols
    
    def save_symbols(self):
        for s in self.all_symbols.values():
            symbol = Symbol(
                exchange='Binance',
                symbol=s["symbol"],
                status=s["status"],
                base_asset=s["baseAsset"],
                base_asset_precision=s["baseAssetPrecision"],
                quote_asset=s["quoteAsset"],
                quote_asset_precision=s["quoteAssetPrecision"],
                quote_precision=s["quotePrecision"],
                order_types=', '.join(s["orderTypes"]))
            self.db.merge(symbol)
        self.db.commit()
