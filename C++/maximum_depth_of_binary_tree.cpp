//no. 104
#include <algorithm>
#include "tree_node.h"
using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root){
            return 0;
        }
        if (!root->left && !root->right){
            return 1;
        }
        int left_ans = maxDepth(root->left) + 1;
        int right_ans = maxDepth(root->right) + 1;
        return max(left_ans, right_ans);
    }
};
