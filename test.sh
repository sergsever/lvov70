#!/bin/bash
PROC=$(cat /proc/cpuinfo)

if [[ $PROC == *"sse4_2"* ]]
then
echo "sse4_2 -ok\n"
else
echo "sse4_2 not found\n"
fi
if [[ $PROC == *"pse"* ]]
then
echo "pse - ok\n"
else
echo "pse not found.\n"
fi
