#!/bin/bash
sed -n '/.*[[:upper:]]$/p' /usr/share/dict/words
