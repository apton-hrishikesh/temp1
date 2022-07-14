#!/bin/bash
x=1
while [ $x -le 50 ]
do
    y=1
    fact=0
    while [ $y -le $x ]
    do
        if [ $(($x / $y)) -eq 1 ];then
        fact=$(( $fact+1 ))
        fi
    done
    
    if [ $fact -eq 2 ];then
        echo $x
    fi
    
    x=$(( $x+1 ))
done
