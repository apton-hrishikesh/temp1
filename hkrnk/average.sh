#!/bin/bash
read n
i=0
sum=0
while [ $i -lt $n ]
do
    read val
    sum=$(( $sum+$val ))
    i=$(( $i+1 ))
done

#echo $( "scale=3; $(( $sum/$n ))" | bc -l)
printf "%.3f\n" $((10**6 * sum/n))e-6

#Divide after multiplying with 1000000 and then cut off at 3 decimal places, roundoff can be #done easier
