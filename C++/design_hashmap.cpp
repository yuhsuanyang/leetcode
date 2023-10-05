//no.706
#include <iostream>
using namespace std;

struct Node {
    int key;
    int val;    
    Node *next;
    Node() : key(0), val(0), next(nullptr) {}
    Node(int x, int y) : key(x), val(y), next(nullptr) {}
    Node(int x, int y, Node *next) : key(x), val(y), next(next) {}
 };

class MyHashMap{
    Node* list;
    public:
        MyHashMap(){
            list= new Node(-1, -1);
        }
        void put(int key, int value){
            Node* curr = list;
            while(curr){
                if(curr->key == key){
                    curr -> val = value;
                    return;
                }
                if(!curr->next){
                    curr -> next = new Node(key, value);
                    return;
                }
                curr = curr -> next;
            }
        }

        int get(int key){
            Node* curr = list;
            while(curr){
                if(curr->key == key){
                    return curr->val;
                }
                curr = curr->next;
            }
            return -1;
        }

        void remove(int key){
            Node* curr = list;
            while(curr){
                if(curr->next){
                    if(curr->next->key == key){
                    curr->next = curr->next->next;
                    break;
                    }
                }
                curr = curr->next;
            }
        }
};


