#include<iostream>
#include<cstdlib>
using namespace std;
void swap(int *one,int *two)
{
	int temp=*one;
	*one=*two;
	*two=temp;
}

int quicksorthelper(int *a,int l,int r,int pivotindex)
{int pivotelement=a[pivotindex];
swap(&a[l],&a[pivotindex]);
int i=l+1;
for(int j=i;j<=r;j++)
	if(a[j]<pivotelement)
		{swap(&a[j],&a[i]);i++;}
swap(&a[l],&a[i-1]);
return i-1;
}

void findkthelement(int *a,int i,int n,int k)
{
	int randompivot=i+rand()%(n-i+1);
	int randomindex=quicksorthelper(a,i,n,randompivot);
	if(randomindex+1==k)
		cout<<a[randomindex];
	else if(randomindex+1>k)
		findkthelement(a,i,randomindex-1,k);
	else
		findkthelement(a,randomindex+1,n,k);
}
int main()
{
	int n,k;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
		cin>>a[i];
	cin>>k;
	if(k>0&&k<=n)
	findkthelement(a,0,n-1,k);
	else
	cout<<"K is not valid"<<endl;
	return 0;
}