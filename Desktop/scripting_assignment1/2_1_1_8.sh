#!/bin/bash
sed -n '/^.....$\|^..........$/p' /usr/share/dict/words|sed '/[^[:upper:]]/p'
