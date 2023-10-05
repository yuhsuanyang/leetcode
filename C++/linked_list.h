#ifndef ListNode_H 
#define ListNode_H

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(0) {}
     ListNode(int x) : val(x), next(0) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#endif
