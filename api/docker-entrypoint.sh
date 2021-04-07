#!/bin/bash

. /venv/bin/activate
uvicorn api.app:app --host 0.0.0.0
