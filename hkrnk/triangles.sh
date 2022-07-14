#!/bin/bash
read x
read y
read z

if [ $x -eq $y ] || [ $x -eq $z ]
then
    if [ $x -eq $y ] && [ $y -eq $z ];then 
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
elif [ $y -eq $z ];then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
