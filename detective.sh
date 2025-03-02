#!/bin/sh

set -e # Exit early if any commands fail

PYTHONPATH=$(dirname $0) exec python3 -m app.main "$@"
