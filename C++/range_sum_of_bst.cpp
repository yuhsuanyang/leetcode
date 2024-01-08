// no. 938
#include "tree_node.h"
#include <vector>
using namespace std;

class Solution {
public:
  int rangeSumBST(TreeNode *root, int low, int high) {
    vector<TreeNode *> queue;
    queue.push_back(root);
    int ans = 0;
    while (!queue.empty()) {
      TreeNode *curr_node = queue.front();
      queue.erase(queue.begin());
      if (curr_node) {
        if (curr_node->val > high) {
          queue.push_back(curr_node->left);
        } else if (curr_node->val < low) {
          queue.push_back(curr_node->right);
        } else {
          ans += curr_node->val;
          queue.push_back(curr_node->left);
          queue.push_back(curr_node->right);
        }
      }
    }
    return ans;
  }
};
