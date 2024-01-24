// no. 94
#include "tree_node.h"
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> result;
  void helper(TreeNode *root) {
    if (!root) {
      return;
    }
    if (root->left) {
      helper(root->left);
    }
    result.push_back(root->val);
    if (root->right) {
      helper(root->right);
    }
  }
  vector<int> inorderTraversal(TreeNode *root) {
    helper(root);
    return result;
  }
};
