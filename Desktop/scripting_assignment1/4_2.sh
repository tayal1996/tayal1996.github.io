#!/bin/bash
x=`echo $1 | grep "[[:digit:]]" | egrep ".{8}.*" | egrep "[@#$%&*+-=]" | grep -c ""`
if [ $x -eq 1 ];
then
	echo "strong password"

else
	echo "weak password"
fi
