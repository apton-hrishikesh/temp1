read -n 1 c
c=$(echo $c | tr '[:upper:]' '[:lower:]' )

if [ $c = "y" ]
then
    echo "YES"        
else
    echo "NO"
fi
