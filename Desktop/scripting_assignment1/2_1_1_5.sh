#!/bin/bash
sed -n '/[[:punct:]]/p' /usr/share/dict/words
