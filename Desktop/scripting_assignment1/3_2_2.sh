#!/bin/bash
awk '{if($2=="M") print $0 }' marks.txt > males.txt
awk '{if($2=="F") print $0 }' marks.txt > females.txt