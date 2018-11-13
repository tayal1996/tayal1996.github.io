#!/bin/bash
x=`echo $1|grep -o "\..*"`
case $x in
".tar") `tar -xf $1`;;
".tar.gz") `tar -xzf $1`;;
".zip") unzip $1;;
"tar.bz2") `tar -xjf $1`;;
".bz2") `bzip2 -dk $1`;;
esac
