// no. 1457
#include "tree_node.h"
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> value_count;
  int result;
  void traverse(TreeNode *root) {
    value_count[root->val - 1]++;
    if (!root->left && !root->right) {
      int num_odd = 0;
      for (int i : value_count) {
        if (i % 2) {
          num_odd++;
        }
      }
      if (num_odd <= 1) {
        result++;
      }
      value_count[root->val - 1]--;
      return;
    }
    if (root->left) {
      traverse(root->left);
    }
    if (root->right) {
      traverse(root->right);
    }
    value_count[root->val - 1]--;
  }
  int pseudoPalindromicPaths(TreeNode *root) {
    for (int i = 0; i < 9; i++) {
      value_count.push_back(0);
    }
    traverse(root);
    return result;
  }
};
