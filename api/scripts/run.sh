#!/bin/bash

docker run \
    -it \
    -v watchdodge:/data \
    -p 8000:8000 \
    --rm \
    --env DD_TRACE_AGENT_PORT=8126 \
    --env DD_AGENT_HOST=host.docker.internal \
    api
