#!/bin/bash
# For the good of all beings.

set -o xtrace
set -o errexit
set -o pipefail

export FLASK_ENV='development'
export FLASK_APP='run.py'
export FLASK_RUN_HOST='0.0.0.0'

ls -laht

flask run
