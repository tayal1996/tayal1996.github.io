#include<bits/stdc++.h>
using namespace std;
string minrotation(string input)
{
	string s=input+input;
	vector<string> v;
	int n=s.size();
	for(int i=0;i<n;i++)
		v.push_back((s.substr(i,n-1)));
	sort(v.begin(),v.end());
	string result;
	for(auto it=v.begin();it!=v.end();it++)
		if((*it).size()>=n/2)
			{result=(*it).substr(0,n/2);break;}
	return result;
}
int main()
{
	string input;
	cin>>input;
	string output=minrotation(input);
	cout<<output;
}