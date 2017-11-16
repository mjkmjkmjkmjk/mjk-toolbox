#!/bin/bash

set -o errexit -o nounset -o pipefail

URL=$( dcos config show core.dcos_url )
TOK=$( dcos config show core.dcos_acs_token )
A="Authorization: token=${TOK}"
C="Content-Type: application/json"
U="${URL}/service/eng-user-marathon/v2/apps/eng/89900-gcp-core/mjk-uptime/versions"


curl -skSL -X GET -H "${A}" -H "${C}" "${U}" 

