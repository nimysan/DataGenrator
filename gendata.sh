#!/bin/bash
#Filename gendata.sh

for ((i=1; i<=$1; i++))
do
    python script.py data_$i.csv $2 &
done

wait