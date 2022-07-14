!#/bin/bash
echo 'Choose:'
select word in 'Apple' 'Microsoft' 'Samsung' 'Google'
do
	echo "You selected $word"
	break
done
