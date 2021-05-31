#!/bin/bash

docker run -d -v /var/run/docker.sock:/var/run/docker.sock:ro \
          -v /proc/:/host/proc/:ro \
          -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
          --net bridge \
          -p 0.0.0.0:8126:8126/tcp \
          -e DD_API_KEY=$DATADOG_API_KEY \
          --rm \
          --name datadog-docker-agent \
          datadog/agent:latest
