#!/bin/bash

for i in */index.txt
do
	echo -n "$(dirname $i) "
	set -- $(tail -n1 $i)
	if test $1 == 0
	then
		echo offline since $(date --date="@$2")
	else
		echo "$3	$4	$5	$6	$7	$8	$9 online since $(date --date="@$2")"
	fi
done

