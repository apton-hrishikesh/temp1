#!/bin/bash

read x
read y

if [ $x -ge $y ];then
    if [ $x -gt $y ];then
        echo "X is greater than Y"
    else
        echo "X is equal to Y"
    fi
else
    echo "X is less than Y"
fi
