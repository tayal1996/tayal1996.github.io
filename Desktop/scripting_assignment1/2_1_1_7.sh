#!/bin/bash
sed -n -E '/.{20,}/p' /usr/share/dict/words
