//no. 606
#include "tree_node.h"
#include <string>
using namespace std;

class Solution {
public:
    string ans;
    void preorder_traverse(TreeNode* root){
      if(root){
        ans += to_string(root->val);
      }
      if(root->left){
        ans += "(";
        preorder_traverse(root->left);
        ans += ")";
      }
      if(root->right){
        if(!root->left){
          ans += "()";
        }
        ans += "(";
        preorder_traverse(root->right);
        ans += ")";
      }
      if(!root->right & !root->left){
        return;
      }
    }
    string tree2str(TreeNode* root) {
      preorder_traverse(root);
      return ans;
    }
};
