#include "linked_list.h"
#include <iostream>
#include <vector>
using namespace std;

ListNode* create_linked_list(vector<int> list){
    if (!list.size()){
        return NULL;
    }else if(list.size() == 1){
        return new  ListNode(list[0]);
    }
    reverse(list.begin(), list.end());
    ListNode* head = new ListNode(list[1], new ListNode(list[0]));
    for (int i = 2; i < list.size(); i++){
        ListNode* newNode = new ListNode(list[i], head);
        head = newNode;
    }
    return head;
}

void print_linked_list(ListNode* head){
    ListNode* curr = head;
    while(curr){
        cout << curr->val << "->";
        curr = curr->next;
    }
    cout << "null" << endl;
    return;
}

int main(){
    int arr[] = {1, 2, 3, 4, 5};
    int arr_len = end(arr) - begin(arr);
    vector <int> v(arr, arr+arr_len);
    ListNode* linked_list = create_linked_list(v);
    print_linked_list(linked_list);
    return 0;
}
