#! /bin/sh
DATE=`date +%Y-%m-%d`
echo $DATE
TIME=`date +%T`
echo $TIME
_USER=$(id -u -n)
echo $_USER
cwd=$(pwd)
echo $cwd