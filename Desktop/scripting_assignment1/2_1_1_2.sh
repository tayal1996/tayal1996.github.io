#!/bin/bash
sed -n '/^[aeiou].*/p' /usr/share/dict/words | wc -l
