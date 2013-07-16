#!/bin/sh
__exit ()
{
	echo $1
	exit 0
}


o=$(date +%Y-%m-%dT%H%M).txt
test -e $o && __exit $o

ps wh -C ssh-port-shell -o command | while read -r cmd switch port id ip
do
	echo $port $id $ip
done | sort -k 2 > $o

__exit $o
