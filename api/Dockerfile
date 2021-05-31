FROM python:3.9-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN apt update && \
    apt install -y \
        gcc \
        libffi-dev \
        g++ \
        && rm -rf /var/lib/apt/lists/*
WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.5

RUN apt update && \
    apt install -y git && \
    rm -rf /var/lib/apt/lists/*
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

COPY . .
RUN . /venv/bin/activate && poetry build

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /app/dist .
COPY docker-entrypoint.sh ./

RUN . /venv/bin/activate && pip install *.whl

VOLUME /data
EXPOSE 8000

ENV ENV PROD
ENV DD_SERVICE="watchdoge"
ENV DD_ENV="prod"
ENV DD_LOGS_INJECTION=true
ENV DD_TRACE_SAMPLE_RATE="1"
ENV DD_PROFILING_ENABLED=true

CMD ["./docker-entrypoint.sh"]
