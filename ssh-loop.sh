#!/bin/bash

test "$port_min" || port_min="10000" 
test "$port_max" || port_max="15000"
test "$server"   || server="pi.dabase.com"
test "$ssh_opts" || ssh_opts="-l pi -t -t -o BatchMode=yes -o ExitOnForwardFailure=yes -o ConnectTimeout=30 -o ServerAliveInterval=180 -o ServerAliveCountMax=3 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" 
test "$ssh_port" || ssh_port="22"
test "$ssh_host" || ssh_host="127.0.0.1"

function ip_address() {
ip route get 8.8.8.8 2>/dev/null|grep -Eo 'src [0-9.]+'|grep -Eo '[0-9.]+'
}

mac_address() {
cat /sys/class/net/$(ip route get 8.8.8.8 2>/dev/null| awk '{print $5}')/address
}

port=$port_min

while true
do
	logger "Trying to connect to ${server}:${port}"
	ssh -R "${port}:${ssh_host}:${ssh_port}" $ssh_opts $server ${port} $(mac_address) $(ip_address)
	port=`expr $port + 1`
	test $port -ge $port_max && port=$port_min
	sleep 10
done
