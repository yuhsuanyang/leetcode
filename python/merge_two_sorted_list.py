# no. 21
from utils import ListNode
class Solution:
    def mergeTwoSortLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list2.next = self.mergeTwoSortLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoSortLists(list1.next, list2)
            return list1
