#!/bin/bash
awk 'END{print $1,$2,$5}' marks.txt
