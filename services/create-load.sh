#!/bin/bash
 
NAMESPACE="${NAMESPACE:-default}"
MODEL="${MODEL:-seldon-model}"
ITERATIONS="${ITERATIONS:-1000}"
WAIT_TIME="${WAIT_TIME:-0.5}"

counter=1
while [ $counter -le $ITERATIONS ]
do
wget -O- mlproduction.dsiag.ch/seldon/$NAMESPACE/$MODEL/api/v1.0/predictions --post-data '{"data": { "ndarray": [[25000, 189625]]}}' --header='Content-Type:application/json'
sleep $WAIT_TIME
((counter++))
done