 #!/bin/bash
 
 #array in
# loop
#	 check count of arr[0]
#	 store in c[0]
	 
read n

read -a arr1
count=0
s_arr1=( "${arr1[@]/*/0}" )

i=0
j=0

while [ $i -lt $n ]
do
	while [ $j -lt $n ]
	do
		if [ ${arr1[$i]} -eq ${arr1[$j]} ]
		then
			s_arr1[$i]=$(( ${s_arr1[$i]}+1 ))
			#echo "s_arr[i]= ${s_arr1[$i]}, i=$i, j=$j"
		fi
		j=$(( $j+1 ))
		#echo "s_arr[$i] = ${s_arr[$i]}"
	done
	j=0
	i=$(( $i+1 ))
done

i=0
while [ $i -lt $n ]
do
	if [ ${s_arr1[$i]} -eq 1 ]
	then
		echo "Unique: ${arr1[$i]}"
		break
	fi
	i=$(( $i+1 ))
done


#count =0
#for i=0 to n:
#	for j=0 to n:
#		if arr[i] = arr[j]:
#			count[i] = count[i]+1

#for j in count:
#	if j==1:
#	 return j
			
			
#		[1,2,2,1,0]
#		 count = [2,2,2,2,1]

# dict = [1:0,2:1,]
