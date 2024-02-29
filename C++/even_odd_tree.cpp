// no,1609
#include "tree_node.h"
#include <vector>
using namespace std;

class Solution {
public:
  bool validateEvenRow(vector<int> vec) {
    if (vec.back() % 2 == 0) {
      return false;
    }
    for (int i = 0; i < vec.size() - 1; i++) {
      if ((vec[i] >= vec[i + 1]) | (!vec[i] % 2)) {
        return false;
      }
    }
    return true;
  }
  bool validateOddRow(vector<int> vec) {
    if (vec.back() % 2 == 1) {
      return false;
    }
    for (int i = 0; i < vec.size() - 1; i++) {
      if ((vec[i] <= vec[i + 1]) | (vec[i] % 2)) {
        return false;
      }
    }
    return true;
  }
  bool isEvenOddTree(TreeNode *root) {
    vector<TreeNode *> queue;
    queue.push_back(root);
    vector<int> row;
    vector<TreeNode *> next_row;
    bool ans;
    int counter = 0;
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
      if (counter % 2) {
        ans = validateOddRow(row);
      } else {
        ans = validateEvenRow(row);
      }
      if (!ans) {
        return false;
      }
      queue = next_row;
      counter++;
    }
    return true;
  }
};
