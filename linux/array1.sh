#!/bin/bash
arr=( hi hello bei gm)
n=${#arr[@]}
echo $n
for ((i=0; i<$n;i++));do 
echo ${arr[${i}]}; 
done
