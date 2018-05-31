#!/bin/sh
read number
i=1
fact=1
while [ $i -le $number ]
do
    fact=$( expr "$i" '*' "$fact")
    i=$((i+1))
done
echo $fact