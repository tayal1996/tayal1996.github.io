#!/bin/bash
sed -n -E '/^(.).*\1$/p' /usr/share/dict/words
