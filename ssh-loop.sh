#!/bin/bash

test "$port_min" || port_min="10000"
test "$port_max" || port_max="15000"
test "$server"   || server="sg.webconverger.com"
test "$ssh_opts" || ssh_opts="-l pi -o ExitOnForwardFailure=yes -T -o RequestTTY=no"
test "$ssh_port" || ssh_port="22"
test "$ssh_host" || ssh_host="127.0.0.1"

function ip_address() {
ip route get 8.8.8.8 2>/dev/null|grep -Eo 'src [0-9.]+'|grep -Eo '[0-9.]+'
}

# TODO: MAC address
# TODO: IPv6 if available
# TODO: sshkey finger print (how does one get this?!)

port=$port_min
while test -e /etc/machine-id
do
	id=$(cat /etc/machine-id)
	logger "Trying to connect to ${server}:${port}"
	ssh -R "${port}:${ssh_host}:${ssh_port}" $ssh_opts $server "${port} ${id}" $(ip_address)
	port=`expr $port + 1`
	test $port -ge $port_max && port=$port_min
	sleep 10
done

sleep 10
