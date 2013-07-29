#!/bin/sh
cat <<END
Cache-Control: no-cache
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Singapore Rasbperry PIs</title>
<style>
	BODY { margin: 10pt; font: 15px/1.25 "Helvetica Neue", sans-serif; }
	p,h1,pre { color: #000; text-shadow: 1px 0 0 #fff, 0 -1px 0 #fff, 0 1px 0 #fff, -1px 0 0 #fff; }
	IMG { clear: both; margin-bottom: 5px; }
	PRE { margin: 20pt; }
	DIV { margin: 20pt; }
</style>
</head>
<body>

<h1>FREE SG based IPv4 port forwarding / concentrator service for their Raspberry PI</h1>

<h2>Why?</h2>

<ul>
<li>If you have trouble figuring out your IP address of your device</li>
<li>Do not have access to the port forwarding UI of your router</li>
</ul>

<p>Running <code>ssh-loop-sh</code> effectively "phones home" and allows you to connect to it, no matter how it's deployed.</p>
<pre>
KEY			PORT	MAC			LOCAL IP	ORIGIN IP	OPORT	HOST		HPORT
END

for i in d/*
do
	{ echo -n "$(basename $i) "; cat $i; } | tr ' ' '\t'
done

cat <<END
</pre>

<h3>Connecting to your PI</h3>
<code>
ssh pi.dabase.com -p \$port # -o "StrictHostKeyChecking no" -o UserKnownHostsFile=/dev/null
</code>

<h3>Setup</h3>

<p>ssh-keygen without a password.</p>

<p>Send hendry@iki.fi your public key /root/.ssh/id_rsa.pub. Once he's added your key, run <a href=ssh-loop.sh>ssh-loop.sh</a>.</p>

<p>To keep it running add to /etc/rc.local like so:</p>

<pre>
#!/bin/sh -e
/root/ssh-loop.sh &
exit 0
</pre>

<p>or use a more "modern" systemd service file <a href=ssh-loop.service>ssh-loop.service</a>.</p>

<h3>How the server works</h3>

<pre><code>$ cat /home/pi/.ssh/authorized_keys
command="/home/pi/pilog hendry" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTK9CFLI4uRI+n5n74WJpvLyS3PdYmgqTDUP/BPRVB9IN8Xt9NZcA5S5/L6VFXujo29rBlLBr4m2jdZoCXKOfoC5VEUEAmX++vDXG42jkzUPLsiMhjJtEgN+YVt3LEkH1REUCDo/AL3SxLVRNvPRHEBLdOyhxmQQrBbosi8rEyjXUsYBY2rhR8RFPcPGpG2NCEjH0gJoLpYIII+BhRRXObCphuhW9QWAzIp7OvxqPjOHDq4HVotcbTWC90ha+n/ZFZ5LOipQG0yQ8Jo5dxbYUZl1iJhKYP2OyTs+3UeIcRnpHvS2Z1+mbzjxpdIVP3sm2HVfXgj+53i7ZtOoQEsNix root@pihsg

$ cat /home/pi/pilog
#!/bin/bash
pi=/srv/www/pi.dabase.com/d/\$1-\$(date +%s)
trap "rm -f \$pi" EXIT
echo \$SSH_ORIGINAL_COMMAND \$SSH_CONNECTION &gt; \$pi
cat &gt; /dev/null
</code></pre>

<p>Tweaks to /etc/ssh/sshd_config to make it work:</p>

<pre><code>
GatewayPorts yes
TCPKeepAlive yes
ClientAliveInterval 10
</code></pre>

<p>For <a href="http://archpi.dabase.com/">more PI tricks and tips</a>.</p>

</body>
</html>
END
