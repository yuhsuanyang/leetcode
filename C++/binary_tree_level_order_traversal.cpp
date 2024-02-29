// no.102
#include "tree_node.h"
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    vector<vector<int>> ans;
    if (!root) {
      return ans;
    }
    vector<int> row;
    vector<TreeNode *> next_row;
    vector<TreeNode *> queue;
    queue.push_back(root);
    while (!queue.empty()) {
      row.clear();
      next_row.clear();
      for (TreeNode *node : queue) {
        row.push_back(node->val);
        if (node->left) {
          next_row.push_back(node->left);
        }
        if (node->right) {
          next_row.push_back(node->right);
        }
      }
      ans.push_back(row);
      queue = next_row;
    }
    return ans;
  }
};
