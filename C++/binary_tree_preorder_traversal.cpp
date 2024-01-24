// no. 144
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
    result.push_back(root->val);
    if (root->left) {
      helper(root->left);
    }
    if (root->right) {
      helper(root->right);
    }
  }
  vector<int> preorderTraversal(TreeNode *root) {
    helper(root);
    return result;
  }
};
