# Goal
This is a playground project aiming at building a dashboard/news aggregator/portfolio view for Bitcoin and other coins.

## Quickstart
```bash
cd api
export CRYPTOGRAPHY_DONT_BUILD_RUST=1
poetry install
poetry run uvicorn api.app:app
poetry run pytest
```

## Running with Datadog agent
```bash
poetry shell
DD_SERVICE="watchdoge" DD_ENV="prod" DD_LOGS_INJECTION=true DD_TRACE_SAMPLE_RATE="1" DD_PROFILING_ENABLED=true ddtrace-run uvicorn api.app:app
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
