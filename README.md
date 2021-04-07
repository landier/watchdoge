# Goal
This is a playground project aiming at building a dashboard/news aggregator/portfolio view for Bitcoin and other coins.

```bash
cd api
export CRYPTOGRAPHY_DONT_BUILD_RUST=1
poetry install
poetry run  uvicorn api.app:app
```
# API endpoints

* /users
* /users/[id]/wallets
* /users/[id]/assets
* /users/[id]/positions
* /users/[id]/transactions
* /tickers
