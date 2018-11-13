#!/bin/bash
sed -n '/Anycity/p' address-book.csv | sed 's/,.*//'
