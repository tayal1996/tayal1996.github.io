#!/bin/bash
sed -n 's/[[:punct:]]/*/gp' address-book.csv | sed -n 's/[0-9]/?/gp'

