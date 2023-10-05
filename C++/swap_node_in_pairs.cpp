//no.24

#include "linked_list.h"

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if((!head) || (!head->next)){
            return head;
        }
        ListNode* sublist = head->next->next;
        ListNode* newHead = head->next;
        head->next = swapPairs(sublist);
        newHead->next = head;
        return newHead;
    }
};
