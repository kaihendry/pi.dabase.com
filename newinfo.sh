cat <<END
<table>
<thead>
<tr>
<th>Name</th>
<th>Port</th>
<th>Mac Address</th>
<th>Local IP</th>
<th>Origin IP</th>
<th>Origin port</th>
<th>Host</th>
<th>Host port</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
END

for i in */index.txt
do
	echo "<tr>"
	echo "<td>$(dirname $i)</td>"
	set -- $(tail -n1 $i)
	if test $1 == 0
	then
		echo "<td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>offline since $(date --date="@$2")</td>"
	else
		echo "<td>$3</td><td>$4</td><td>$5</td><td>$6</td><td>$7</td><td>$8</td><td>$9</td><td>online since $(date --date="@$2")</td>"
	fi
	echo "</tr>"
done

cat <<END
</tbody>
</table>
END
