// no. 98
#include "tree_node.h"
#include <string>
using namespace std;

class Solution {
public:
  bool ans = true;
  int get_extreme(TreeNode *root, string mode) {
    int left = root->val;
    int right = root->val;
    if (root->left) {
      left = get_extreme(root->left, mode);
      if ((mode == "max") & (left >= root->val)) {
        ans = false;
      }
    }
    if (root->right) {
      right = get_extreme(root->right, mode);
      if ((mode == "min") & (right <= root->val)) {
        ans = false;
      }
    }
    if (mode == "max") {
      return max(left, right);
    } else {
      return min(left, right);
    }
  }
  bool isValidBST(TreeNode *root) {
    get_extreme(root, "max");
    if (ans) {
      get_extreme(root, "min");
    }
    return ans;
  }
};
