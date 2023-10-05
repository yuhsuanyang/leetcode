# no. 108
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        print(self.left, self.val, self.right)


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not len(nums):
            return None
        middle = len(nums) // 2
        node = TreeNode(val=nums[middle],
                        left=self.sortedArrayToBST(nums[:middle]),
                        right=self.sortedArrayToBST(nums[middle + 1:]))
        print(hex(id(node)))
        print('-----------')
        return node


sol = Solution()
print(sol.sortedArrayToBST([-10, -3, 0, 5, 9]))
