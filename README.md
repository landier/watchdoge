# Goal
This is a playground project aiming at building a dashboard/news aggregator/portfolio view for Bitcoin and other coins.

```bash
cd api
export CRYPTOGRAPHY_DONT_BUILD_RUST=1
poetry install
poetry run  uvicorn api.app:app
poetry run pytest
```

# Docs
* (https://python-binance.readthedocs.io/en/latest/)
* (https://github.com/sammchardy/python-binance/)
* (https://github.com/binance-exchange/mytrades-downloader)
* (https://www.uvicorn.org/)
# API endpoints

* /users
* /users/[id]/wallets
* /users/[id]/assets
* /users/[id]/positions
* /users/[id]/trades
* /tickers
