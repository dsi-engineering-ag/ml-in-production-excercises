#!/bin/bash

podman manifest create docker.io/fluescher/jupyter:2025-hs
podman build . --manifest docker.io/fluescher/jupyter:2025-hs --platform linux/arm64,linux/amd64
podman manifest push --all docker.io/fluescher/jupyter:2025-hs
podman tag docker.io/fluescher/jupyter:2025-hs docker.io/fluescher/jupyter:latest
podman manifest push --all docker.io/fluescher/jupyter:latest