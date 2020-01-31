for i in `seq 1 100`;
do
    if ((i % 7)); then
        echo $i >> check.txt
    else
	echo 7 >> check.txt
    fi        
done

cat table.csv | cut -d ',' -f4 | egrep '\.png$' | sed -e "s/^junk//" |sort -d | sed -e "s/[1-9]//" | grep -o '^[^\.]*' > magic




echo 'while :; do sleep 1; done' > dragonfly.sh

sudo -u testUser ./dragonfly.sh &
sudo su - c "./dragonfly.sh &" testUser






#!/bin/bash

function boogiewoogie() {
  for (( c=1; c<=$1; c++ ))
    do
      echo 'I like to boogiewoogie every day!'
    done
}




