#!/bin/bash

trap bashtrap INT	
clear;			

bashtrap()
{
	echo "CTRL+C detected-- Bashtrap triggered"
}
for a in `seq 1 10`;do
	echo "$a/10 to Exit."
	sleep 3;
done
echo "Bashtrap action complete"
