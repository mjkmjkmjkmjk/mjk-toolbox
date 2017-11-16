#!/bin/bash

set -o errexit -o nounset -o pipefail

U=$( dcos config show core.dcos_url )
TOK=$( dcos config show core.dcos_acs_token )
AUT="Authorization: token=${TOK}"


URL="${U}/service/marathon-user/v2/events"

curl -skSL \
    -H "${AUT}" \
    -H "Accept: text/event-stream"  \
    "${URL}"

