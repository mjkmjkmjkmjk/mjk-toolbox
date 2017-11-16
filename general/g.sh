#!/bin/bash

set -o errexit -o nounset -o pipefail

URL=$( dcos config show core.dcos_url )
TOK=$( dcos config show core.dcos_acs_token )
A="Authorization: token=${TOK}"
C="Content-Type: application/json"
U="${URL}/marathon/v2/leader"

U="${URL}/mesos/master/state.json"


# Get from all MoMs;
for xx in eng prod test dev;do 
  U="${URL}/service/${xx}-user-marathon/v2/apps"
  echo $U
  curl -skSL -X GET -H "${A}" -H "${C}" "${U}"|jq . > ${xx}.JSON
done

