#!/usr/bin/env bash

set -o errexit -o pipefail -o nounset
APP_ID="${1}"
KEY="${2}"
VALUE="${3}"
dcos marathon app show "${APP_ID}" \
  | jq '. | del(.tasks, .tasksHealthy, .tasksRunning, .tasksStaged, .tasksUnhealthy, .version, .versionInfo)' \
  | jq ".${KEY} = \"${VALUE}\""  #  | dcos marathon app update "${APP_ID}"
