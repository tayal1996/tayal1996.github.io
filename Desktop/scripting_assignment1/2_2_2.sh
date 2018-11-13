#!/bin/bash
sed -n '/^[^aeiouAEIOU]/p' address-book.csv
