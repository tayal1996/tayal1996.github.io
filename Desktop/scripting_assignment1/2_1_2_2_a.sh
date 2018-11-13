#!/bin/bash
sed -n -E '/[[:digit:]]{3}\.[[:digit:]]{3}\.[[:digit:]]{3}\.[[:digit:]]{3}/p' $1
