#!/bin/bash

URL="https://maker.ifttt.com/trigger"
EVENTNAME="raspberry_pi"
YOUR_KEY="bBAMXFrNxtNPmk8wUKMVl"

WEBHOOKSURL="${URL}/$[EVENTNAME}/with/key/${YOUR_KEY}"

curl -X POST -H "Content-Type: application/json" -d \
        '["Value1":"'$1'","Value2":"'$2'","Value3":"'$3'"]' \
        ${"WEBHOOKSURL"}

echo
exit 0
