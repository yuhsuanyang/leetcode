// no. 19
#include "linked_list.h"

class Solution {
public:
  int getLength(ListNode *head) {
    int counter = 0;
    ListNode *curr = head;
    while (curr) {
      counter++;
      curr = curr->next;
    }
    return counter;
  }
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    int list_len = getLength(head);
    int m = list_len - n;
    ListNode *curr = head;
    if (m == 0) {
      return curr->next;
    }
    for (int i = 0; i < m - 1; i++) {
      curr = curr->next;
    }
    curr->next = curr->next->next;
    return head;
  }
};
