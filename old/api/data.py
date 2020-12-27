from dataclasses import dataclass
from decimal import Decimal
import arrow

@dataclass
class Transaction:
    transaction_id: str
    amount: Decimal
    currency: str


@dataclass
class Balance:
    timestamp: int
    amount: Decimal
    currency: str


@dataclass
class ExchangePlatform:
    name: str
    api_key: str
    secret_key: str


class DataStore(dict):
    def add(self, key, value):
        self[key] = value

    def list(self):
        return list(self.items())


class Ledger:
    def __init__(self, currency):
        self.currency = currency
        self.history = {}
        self.last_balance = None

    def __repr__(self):
        return repr(self.history)

    def add_balance(self, timestamp: str, amount: Decimal):
        self.history[timestamp] = amount

    def get_balance_at(self, timestamp: str):
        for key in sorted(self.history.keys(), reverse=True):
            if key > timestamp:
                continue
            if key < timestamp:
                return self.history[key]

    def get_current_balance(self):
        try:
            return self.history[max(self.history.keys())]
        except ValueError:
            return None


class GeneralLedger:
    def __init__(self):
        pass


if __name__ == '__main__':
    # Given
    btc_ledger = Ledger('btc')

    # When
    btc_ledger.add_balance('2019-04-01', Decimal(4))
    btc_ledger.add_balance('2019-06-01', Decimal(6))
    btc_ledger.add_balance('2019-03-01', Decimal(3))
    btc_ledger.add_balance('2019-05-01', Decimal(5))

    # Then
    print(btc_ledger)
    assert btc_ledger.get_current_balance() == Decimal(6)
    assert btc_ledger.get_balance_at('2019-05-10') == Decimal(5)
