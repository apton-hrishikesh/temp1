#!/bin/bash
X=1

while [ $X -le 99 ]; do
    echo $X
    let X=X+2
done
