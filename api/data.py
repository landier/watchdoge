from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Transaction:
    transaction_id: str
    amount: Decimal
    currency: str


@dataclass
class Balance:
    exchange_id: str
    timestamp: int
    amount: Decimal
    currency: str


@dataclass
class ExchangePlatform:
    name: str
    api_key: str
    secret_key: str
