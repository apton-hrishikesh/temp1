#!/bin/bash
VAR="Global"

function test {
local VAR="Local"
echo $VAR
}

echo $VAR

test

echo $VAR
