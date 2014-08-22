#!/bin/bash

cat <<END
Cache-Control: no-cache
Content-Type: text/plain

END


for i in */
do
	test -f "$i/index.txt" || continue
	tail -n1 $i/index.txt | while read -p _ on _ port _ _ _ _
	do
		if test "$on" -eq 1
		then
		echo -n "$i "
		ssh -t -t -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o PreferredAuthentications=none localhost -p $port 2>&1 | grep -v Warn
		fi
	done
done
