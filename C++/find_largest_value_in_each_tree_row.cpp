//no.515
#include <vector>
#include "tree_node.h"
using namespace std;

class Solution {
public:
    vector<int>vals;
    vector<int> largestValues(TreeNode* root) {
      vector<int> ans;
      if(!root){
        return  ans;
      }
      vector<TreeNode*> cache;
      ans.push_back(root->val);
      cache.push_back(root);
      while(cache.size()){
        vals.clear();
        vector<TreeNode*> new_cache;
        for(int i=0; i <= cache.size(); i++){
          TreeNode* left = cache[i]->left;
          TreeNode* right = cache[i]->right;
          if(left){
            if(vals.empty() or left->val > vals.back()){
              vals.push_back(left->val);
            }
            new_cache.push_back(left);
          }
          if(right){
            if(vals.empty() or right->val > vals.back()){
              vals.push_back(right->val);
            }
            new_cache.push_back(right);
          }
        }
        if(!vals.empty()){
          ans.push_back(vals.back());
        }
        cache = new_cache;
      }
      return ans;
    }

};
