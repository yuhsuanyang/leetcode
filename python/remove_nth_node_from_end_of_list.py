# no.19
from utils import ListNode 
class Solution:
    def get_length(self, head):
        counter = 0
        curr = head
        while curr:
            counter += 1
            curr = curr.next
        return counter

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = self.get_length(head)
        m = list_len - n
        curr = head
        if m == 0:
            return curr.next
        for i in range(m - 1):
            curr = curr.next
        curr.next = curr.next.next
        return head

