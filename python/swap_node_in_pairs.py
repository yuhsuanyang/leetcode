# no.24
from utils import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        sublist = head.next.next
        new_head = head.next
        head.next = self.swapPairs(sublist)
        new_head.next = head
        return new_head

