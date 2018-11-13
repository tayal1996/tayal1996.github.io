#include<iostream>
#include<new>
#include<vector>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define MemLimit 1000
using namespace std;

template<typename A, typename T>
struct MapNode{
    A key;
    T value;
    MapNode * next = NULL;
    MapNode(A k, T v){
        key = k;
        value = v;
    }
};

template<class A, class T>
class unordered_map{
    public:
        int mapCapacity;
        int mapSize;
        MapNode<A, T> * map[MemLimit] = {NULL};

        unordered_map();

        int CalculateIndex(string const& Str);
        int HashFunction(int Key);
        int HashFunction(string Key);
        int HashFunction(double Key);
        int HashFunction(float Key);
        int HashFunction(long long int Key);
        void insert(A, T);
        void erase(A);
        int size();
        T operator [](A);
};

template<typename A,typename T> 
unordered_map<A, T>::unordered_map(){
    mapCapacity = MemLimit;
    mapSize = -1;
}

template<typename A,typename T>
int unordered_map<A, T>::CalculateIndex(const string &Str) {
    int hash = 5381;
    for (auto it: Str)
        hash = (hash << 5) + hash * 33 + it;
    return hash % MemLimit;
}

template<typename A,typename T>
int unordered_map<A, T>::HashFunction(int Key){
    return CalculateIndex(to_string(Key));
}

template<typename A,typename T>
int unordered_map<A, T>::HashFunction(string Key){
    return CalculateIndex(Key);
}

template<typename A,typename T>
int unordered_map<A, T>::HashFunction(double Key){
    return CalculateIndex(to_string(Key));
}

template<typename A,typename T>
int unordered_map<A, T>::HashFunction(float Key){
    return CalculateIndex(to_string(Key));
}

template<typename A,typename T>
int unordered_map<A, T>::HashFunction(long long int Key){
    return CalculateIndex(to_string(Key));
}

template<typename A,typename T>
void unordered_map<A, T>::insert(A Address, T value){
    int index = HashFunction(Address);
    MapNode<A, T> * StartNode = new MapNode<A, T>(Address, value);
    if(map[index] != NULL){
        MapNode<A, T> * NewNode = map[index];
        while(NewNode->next != NULL && NewNode->key != Address)
            NewNode = NewNode->next;
        if(NewNode->key == Address)
            NewNode->value = value;
        else NewNode->next = StartNode; 
    }
    else map[index] = StartNode;
    mapSize++; 
}

template<typename A,typename T>
int unordered_map<A, T>::size(){
    return mapSize+1;
}

template<typename A,typename T>
T unordered_map<A, T>::operator [](A Address){
    int index = HashFunction(Address);
    MapNode<A, T> * Node = map[index];
    if(Node == NULL) return 0;
    
    while(Node->next != NULL){
        if(Node->key == Address) return Node->value;
        Node = Node->next;
    }
    return (Node->key == Address ? Node->value : 0);
}

template<typename A,typename T>
void unordered_map<A, T>::erase(A Address){
    int index = HashFunction(Address);
    MapNode<A, T> * Node = map[index];
    if(Node == NULL) return ;
    if(Node->next == NULL && Node->key == Address){
        free(Node->next);
        Node = NULL;
        return ;
    }
    if(Node->key == Address){

    }
    if(Node->next != NULL){
        while(Node->next->key != Address && Node->next->next != NULL)
            Node->next = Node->next->next;
    }
    
    if(Node->next->key == Address){
        MapNode<A, T> * TempNode = Node->next;
        Node = Node->next->next;
        free(TempNode);
    }
    cout<<"Not exist!\n";
}

int main(){
    // unordered_map<string, int> m;
    unordered_map<int, int> m1;
    // m.insert("A", 10);
    // m.insert("B", 10);
    // m.insert("C", 10);
    // m.insert("D", 10);
    // m.insert("E", 10);
    // m.insert("F", 10);
    // cout<<m["B"]<<"\n";
    for(int i = 0; i < 999999; i++)
        m1.insert(i,10);

    // for(int i = 0; i < 999999; i++){
    //  cout<<m1[i]<<" ";
    // }
    cout<<m1.size()<<"\n";
    
    // unordered_map<string, string> m2;
    // m2.insert("Lal", "Giridhari");
    // m2.insert("Lal", "Sumit");
    // cout<<m2["Lal"]<<"\n";
    // cout<<m2.size()<<" ";
    
    // m2.erase("Lal");
    // cout<<m2.size()<<" ";
    // cout<<m2["Lal"]<<" ";

    // unordered_map<int, string> m3;
    // m3.insert(2,"Giridhari");
    // m3.insert(3,"Lal Gupta");
    // m3.insert(4,"Sumit");

    // cout<<m3[2]<<" ";
    // cout<<m3[3]<<" ";
    // cout<<m3[4]<<" ";

    // m3.insert(3,"Shilpi");
    // cout<<m3[3]<<" ";
    return 0;
}