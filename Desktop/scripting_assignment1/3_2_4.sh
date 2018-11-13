#!/bin/bash
awk 'BEGIN{max=0; avg=0; a[0]=0; n[0]="";}{if(NR!=1){a[NR]=($3+$4+$5); n[NR]=$1; avg=avg+a[NR]; if(max<a[NR]){max=a[NR]; name=$1;}}} END{avg=avg/(NR-1); printf("Topper is %s\nAbove Averages are:",name); for(i=2;i<=NR;i++) if(a[i]>avg) printf(" %s",n[i])}' marks.txt

