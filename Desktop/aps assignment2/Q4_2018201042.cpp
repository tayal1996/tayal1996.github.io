#include <bits/stdc++.h>
using namespace std;
#define hashsize 1000
struct node
{
	string key;
	string value;
	struct node *next;
};

struct hashtable
{
	struct node *head;
	struct node *tail;
};

int size=0;
struct hashtable mytable[hashsize];

int hashvalue(string key)
{
	int sum=0;
	if(isdigit(key[0]))
		return stoi(key)%hashsize;
	for(int i=0;key[i]!='\0';i++)
		{
			if(isupper(key[i]))
				sum+=(key[i]-'A')*(i+1);
			else
				sum+=(key[i]-'a')*(i+1);
		}
	return sum%hashsize;

}

string find(string key)
{
	int hashval=hashvalue(key);
	struct node *list=(struct node*)mytable[hashval].head;
	while(list)
	{
		if(list->key==key)
			return list->value;
		else
			list=list->next;
	}
	return "-1";
}

struct node* getnode(string key)
{
	int hashval=hashvalue(key);
	struct node *list=(struct node*)mytable[hashval].head;
	while(list)
	{
		if(list->key==key)
			return list;
		else
			list=list->next;
	}
	return NULL;
}

void insert(string key,string value)
{
	struct node* f=getnode(key);
	if(f==NULL)
	{	size++;
		int hashval=hashvalue(key);
		cout<<"\n#"<<hashval;
		// struct node *now=(struct node*) malloc(sizeof(struct node));
		node *now=new node;
		now->key=key;
		now->value=value;
		now->next=NULL;
	
		if(mytable[hashval].head==NULL)
			{
				mytable[hashval].head=now;
				mytable[hashval].tail=now;
			}
		else
			{
				mytable[hashval].tail->next=now;
				mytable[hashval].tail=now;
			}
	}
	else
	{
		f->value=value;
	}
}

void del(string key)
{
	int hashval=hashvalue(key);
	struct node *list=(struct node*)mytable[hashval].head;
	if(list==NULL)
		cout<<"KEY NOT FOUND\n";
	else
	{
		if(list->key==key)
			{mytable[hashval].head=list->next;
			list->next=NULL;
			cout<<"KEY DELETED\n";}
		else{
			while(list->next&&list->next->key!=key)
				list=list->next;
			if(list->next==NULL)
				cout<<"KEY NOT FOUND\n";
			else if(mytable[hashval].tail->key==key)
			{
				list->next=NULL;
				mytable[hashval].tail=list;
				cout<<"KEY DELETED\n";
			}
			else
			{
				list->next=list->next->next;
				cout<<"KEY DELETED\n";
			}

		}

	}
}


int main()
{	
	
	// cout<<"Enter initial size of hash table";
	// cin>>hashsize;
	// mytable = (struct hashtable*) malloc(hashsize * sizeof(struct hashtable*));
	for(int i=0;i<hashsize;i++)
	{
		// mytable[i]=(struct hashtable) malloc(sizeof(struct hashtable));
		mytable[i].head=NULL;
		mytable[i].tail=NULL;
	}
	
	int choice;
	string s1,s2;
	while(1)
	{
		cout<<"\nEnter choice\n1.Insert\n2.Delete\n3.Find\n\n";
		cin>>choice;
		switch(choice)
		{
		case 1: cout<<"Enter key\n";
				cin>>s1;
				cout<<"Enter value\n";
				cin>>s2;
				insert(s1,s2);
				break;
		case 2:	cout<<"Enter key\n";
				cin>>s1;
				del(s1);
				break;
		case 3:	cout<<"Enter key\n";
				cin>>s1;
				s2=find(s1);
				cout<<s2;
				break;
		default:break;
		}
	}

	return 0;
}