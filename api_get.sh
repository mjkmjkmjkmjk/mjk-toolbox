#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "ERROR: Provide an api endpoint string, e.g. 'marathon/v2/apps'"
    exit 3
fi

JQ_TEST=$(jq --version)
if [ $? != 0 ];then
  JQ=''
else
  JQ="$(which jq) ."
fi

A="Authorization: token=$(dcos config show core.dcos_acs_token)"
C="Content-Type: application/json"
CORE="$(dcos config show core.dcos_url)/"

curl -X GET -skSL -H "$A" -H "$C" "${CORE}${1}" | $JQ
