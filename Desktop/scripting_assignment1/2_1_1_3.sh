#!/bin/bash
sed -n '/^[aeiou].*[aeiou]$/p' /usr/share/dict/words | wc -l
