#!/bin/bash
echo -e "Enter a word: \c"
read word
echo "The word you entered is: $word"
echo -e "Enter two words: \c"
read w1 w2
echo "You entered: \"$w1 and \"$w2"
echo "Enter any line or sentence:"
read
echo $REPLY
echo "Enter some words for an array"
read -a arr1
echo "Arr[0-n]=${arr1[0]},${arr1[1]}" 

