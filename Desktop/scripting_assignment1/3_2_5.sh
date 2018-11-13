#!/bin/bash
awk 'BEGIN{printf("\n*** Grade report for the ABC course ***\n"); max=0; avg=0; min=1000000; grade="";}
{sum=($3+$4+$5); avg=avg+sum; if(max<sum){max=sum;} if(sum<min&&NR!=1){min=sum;} if(sum>=95){grade="A";} else if(sum>=90){grade="A-";} else if(sum>=85){grade="B";} else if(sum>=80){grade="B-";} else if(sum>=75){grade="C";} else if(sum>=70){grade="C-";} else if(sum>=60){grade="D";} else{grade="F";} if(NR==1){printf("%s Grades\n",$0);} else {printf("%s %s\n",$0,grade);}} 
END{avg=avg/(NR-1); printf("Maximum marks: %d Minimum marks: %d Average marks: %d Number of students: %d\n*** End of Grade Report ***\n",max,min,avg,NR-1);}' marks.txt


