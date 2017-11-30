L="https://maker.ifttt.com/trigger"
EVENTNAME="raspberry_pi" 
YOUR_KEY="ここにYour keyを入力"
 ?
WEBHOOKSURL="${URL}/${EVENTNAME}/with/key/${YOUR_KEY}"
?
curl -X POST -H "Content-Type: application/json" -d \
????'{"value1":"'$1'","value2":"'$2'","value3":"'$3'"}' \
????${WEBHOOKSURL} 
?
echo
exit 0i
