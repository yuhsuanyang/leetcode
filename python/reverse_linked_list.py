#no. 206
from utils import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last_node
