#!/bin/bash

. /venv/bin/activate
ddtrace-run uvicorn api.app:app --host 0.0.0.0
