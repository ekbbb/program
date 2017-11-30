#!/bin/sh

string="hi,hosoya!"

echo string
echo 'string'
echo "string"
echo
echo $string
echo '$string'
echo "$string"
echo
echo ${string}
echo '${string}'
echo "${string}"
echo

num=8

echo num
echo 'num'
echo "num"
echo
echo $num
echo '$num'
echo "$num"
echo
echo ${num}
echo '${num}'
echo "${num}"
echo

name=naoki
age=19

echo '$name is $age years old.'
echo "$name is $age years old."
echo
printf '%s is %d years old.\n' $name $age
printf "%s is %d years old.\n" $name $age
