# no. 606
class Solution:
    def __init__(self):
        self.ans = ''
    def preorder_traverse(self, root):
      if root:
        self.ans += f'{root.val}'
      if root.left:
        self.ans += '('
        self.preorder_traverse(root.left)
        self.ans += ')'
      if root.right:
        if not root.left:
          self.ans += '()'
        self.ans += '('
        self.preorder_traverse(root.right)
        self.ans += ')'
      if not root.left and not root.right:
        return

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.preorder_traverse(root)
        return self.ans
