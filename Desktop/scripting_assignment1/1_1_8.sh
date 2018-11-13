#!/bin/bash
 egrep '^.....$'\|'^..........$' /usr/share/dict/words|egrep '[^[:upper:]]'