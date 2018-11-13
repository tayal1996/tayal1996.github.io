#!/bin/bash
sed -n -E 's/^([^,]*),([^,]*),(.*)$/\2,\1,\3/p' address-book.csv
