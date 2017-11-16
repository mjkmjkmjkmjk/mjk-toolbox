#!/bin/bash

set -o errexit -o nounset -o pipefail

U=$( dcos config show core.dcos_url )
TOK=$( dcos config show core.dcos_acs_token )
AUT="Authorization: token=${TOK}"

ACTION=$1
JSONFILE=$2
OPTIONAL_ENDPOINT="${3}"

URL="${U}/service/marathon-user/v2/apps"

curl -skSL \
    -X "${ACTION}" \
    -d "@${JSONFILE}" \
    -H "${AUT}" \
    -H "Content-Type: application/json" \
    "${URL}${OPTIONAL_ENDPOINT}"

