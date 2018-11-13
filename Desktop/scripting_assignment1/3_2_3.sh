#!/bin/bash
awk '{if(NR!=1) print $1,($3+$4+$5)}' marks.txt
