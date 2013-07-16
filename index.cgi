#!/bin/sh

latest=$(./list.sh)

cat <<END
Cache-Control: no-cache
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>$(wc -l < $latest) Singapore PI(s) online</title>
<style>
	BODY { margin: 10pt; font: 15px/1.25 "Helvetica Neue", sans-serif; }
	p,h1,pre { color: #000; text-shadow: 1px 0 0 #fff, 0 -1px 0 #fff, 0 1px 0 #fff, -1px 0 0 #fff; }
	IMG { clear: both; margin-bottom: 5px; }
	PRE { margin: 20pt; }
	DIV { margin: 20pt; }
body
{ 
background-image:url('Raspi_Colour_R.png');
background-size: contain;
background-repeat:no-repeat;
background-attachment:fixed;
background-position:center; 
}
	
</style>
</head>
<body>

<h1>FREE SG based IPv4 port forwarding / concentrator service for their Raspberry
PI</h1>

<div>
<!--  if you just want the data:
$ curl -s pi.dabase.com/d/ > /dev/null # Generate record
$ curl -s pi.dabase.com/d/\$(date -u +%Y-%m-%dT%H%M.txt)
-->
PIs currently logged in as of ${latest%.txt}:
</div>
<pre>
PORT  UUID                                 IP
END

cat $latest

cat <<END
</pre>

<h3>Connecting to your PI</h3>
<p>
ssh root@pi.dabase.com -p \$port
</p>

<h3>Setup</h3>

<p>ssh-keygen without a password.</p>

<p>Send hendry@iki.fi your public key /root/.ssh/id_rsa.pub. Once he's added your key, run <a href=ssh-loop.sh>ssh-loop.sh</a>.</p>

<p>To keep it running use inittab like so:</p>

<pre>
X5:2:respawn:/root/ssh-loop.sh
</pre>

<p>or use a more "modern" systemd service file <a href=ssh-loop.service>ssh-loop.service</a>.</p>

</body>
</html>
END
