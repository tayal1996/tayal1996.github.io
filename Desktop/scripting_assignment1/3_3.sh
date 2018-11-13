#!/bin/bash
awk '{gsub(/[()]/,""); print;}' imdb-top-250.txt | awk 'BEGIN{printf("[\n")} {st=""; for(i=2;i<NF-1;i++){st=st $i} if(NR!=250) {printf("{\n\"ID\" : \"%d\" ,\n\"Name\" : \"%s\" ,\n\" Year \" : \"%s\" ,\n\" Rating \" : \"%.1f\"\n} ,\n",$1,st,$(NF-1),$NF)} else {printf("{\n\"ID\" : \"%d\" ,\n\"Name\" : \"%s\" ,\n\" Year \" : \"%s\" ,\n\" Rating \" : \"%.1f\"\n}\n",$1,st,$(NF-1),$NF)} } END{printf("]");}'


