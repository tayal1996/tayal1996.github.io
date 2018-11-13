#include<iostream>
#include<string.h>
using namespace std;
#define stringBuilder stringbuilder*
char gstr[100];
struct stringbuilder
{
char *charpointer;
struct stringbuilder *left;
struct stringbuilder *right;
};

stringbuilder* stringInitialize(char* a)
{
	stringbuilder *temp=new stringbuilder;
	temp->charpointer=a;
	temp->left=NULL;
	temp->right=NULL;
	return temp;
}

stringbuilder* stringAppend(stringbuilder *s1,stringbuilder *s2) 
{
	stringbuilder *temp=new stringbuilder;
	temp->charpointer=NULL;
	temp->left=s1;
	temp->right=s2;
	return temp;
}

void display(stringbuilder *s)
{
	if(s->charpointer!=NULL)
		strcat(gstr,s->charpointer);
	else
		{display((s->left));
		display((s->right));
		}
}

int KMPSearch(char* pat, char* txt) 
{ 
    int M = strlen(pat); 
    int N;
    for(N=0;txt[N]!='\0';N++); 
    	// cout<<N<<"#\n";
    int lps[M]; 

    int len = 0; 
  	lps[0] = 0;

    int i = 1; 
    while(i<M){ 
        if(pat[i]==pat[len]){  
            lps[i++]=++len; 
        } 
        else
            if(len!=0)
            { 
                len=lps[len - 1]; 
            } 
            else
            { 
                lps[i]=0; 
                i++; 
            } 
        } 
     
  
    i=0;
    int j=0;
    while(i<N){ 
		if (pat[j] == txt[i]) { 
            j++; 
            i++; 
        } 
        if(j==M){ 
        	if(i-j==N)
        		return -1;
        	else
            	return i-j; 
        } 
        else if(i<N&&pat[j]!=txt[i]){ 
            if (j!=0) 
                j=lps[j - 1]; 
            else
                i=i+1; 
        } 
    } 
}

int findSubstring(stringbuilder *sb,char *a)
{
strcpy(gstr,"");
display(sb);
int index=KMPSearch(a,gstr);
if(index==strlen(gstr))return -1;
return index;

}

int main()
{
stringBuilder s1=stringInitialize("hello");
stringBuilder s2=stringInitialize("world");
int index1=findSubstring(s2,"or");
int index2=findSubstring(s2,"hell");
stringBuilder s3=stringAppend(s1,s2);
strcpy(gstr,"");
display(s1);
cout<<gstr<<"\n";
strcpy(gstr,"");
display(s2);
cout<<gstr<<"\n";
strcpy(gstr,"");
display(s3);
cout<<gstr<<"\n";
cout<<index1<<" "<<index2<<"\n";
return 0;
}