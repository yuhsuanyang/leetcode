//no. 700
#include "tree_node.h"

class Solution{
    public:
        TreeNode* searchBST(TreeNode* root, int val) {
            if (!root){
                return NULL;
            }
            if (root->val == val){
                return root;
            }
            if (!root->left && !root->right){
                return NULL;
            }
            TreeNode* left_ans = searchBST(root->left, val);
            TreeNode* right_ans = searchBST(root->right, val);
            if (left_ans){
                return left_ans;
            }
            if (right_ans){
                return right_ans;
            }
            return NULL
            

        }
}
