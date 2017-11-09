#!/usr/bin/env bash

set -o errexit -o nounset -o pipefail


if [ $# -ne 2 ];then
  echo "Usage: $0 <hostname or IP>, <duration in hours>"
  exit 4
fi


ONEMINUTEFROMNOW=$( ./one_minute_from_now_in_nanos.py )

IP=$1
HOURS=$2



DU=$(( $HOURS * 60 * 60 * 1000 * 1000 * 1000 ))




HDOC='./mjkheredoc'

cat > ${HDOC} <<HEREDOCUMENT
{
  "windows": [
    {
      "machine_ids": [
        {
          "hostname": "${IP}",
          "ip": "${IP}"
        }
      ],
      "unavailability": {
        "start": {
          "nanoseconds": ${ONEMINUTEFROMNOW}
        },
        "duration": {
          "nanoseconds": ${DU}
        }
      }
    }
  ]
}
HEREDOCUMENT


echo "###### DOC to be used: ###########"
cat $HDOC
echo "##################################"




U=$( dcos config show core.dcos_url )
TOK=$( dcos config show core.dcos_acs_token )
AUT="Authorization: token=${TOK}"
CNT="Content-Type: application/json"

URL="${U}/mesos/metrics/snapshot"


curl -skSL \
    -X GET \
    -H "Authorization: token=${TOK}" \
    -H "Content-Type: application/json" \
    "${URL}" | jq .


set -x
URL="${U}/mesos/maintenance/schedule"
curl -skSL \
    -X POST \
    -d "@${HDOC}" \
    -H "Authorization: token=${TOK}" \
    -H "Content-Type: application/json" \
    "${URL}"  | jq .


echo ""
echo ""
echo "Maintenance Status:"
echo ""
echo ""

URL="${U}/mesos/maintenance/status"

curl -skSL \
    -X GET \
    -H "Authorization: token=${TOK}" \
    -H "Content-Type: application/json" \
    "${URL}" | jq .
