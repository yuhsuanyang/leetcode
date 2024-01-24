// no. 145
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
    if (root->right) {
      helper(root->right);
    }
    result.push_back(root->val);
  }
  vector<int> postorderTraversal(TreeNode *root) {
    helper(root);
    return result;
  }
};
