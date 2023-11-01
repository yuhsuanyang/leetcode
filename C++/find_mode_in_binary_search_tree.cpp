//no. 501
#include <vector>
#include <map>
#include "tree_node.h"
using namespace std;

class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        vector<int> ans;
        if(!root->left & !root->right){
            ans.push_back(root->val);
            return ans;
        }
        vector<TreeNode*> cache;
        map<int, int> counter;
        counter[root->val] = 1;
        int max_ = 1;
        cache.push_back(root);
        while(cache.size()){
            TreeNode* temp = cache[0];
            cache.erase(cache.begin());
            if(temp->left){
                cache.push_back(temp->left);
                if (counter.find(temp->left->val) == counter.end()){
                    counter[temp->left->val] = 1;
                }else{
                    counter[temp->left->val] += 1;
                }   
                if (counter[temp->left->val] > max_){
                    max_ = counter[temp->left->val];
                }
            }
            if(temp->right){
                cache.push_back(temp->right);
                if (counter.find(temp->right->val) == counter.end()){
                    counter[temp->right->val] = 1;
                }else{
                    counter[temp->right->val] += 1;
                }   
                if (counter[temp->right->val] > max_){
                    max_ = counter[temp->right->val];
                }
            }
        }
        for (map<int, int>::iterator iterator = counter.begin(); iterator != counter.end(); iterator ++){
            if (iterator->second == max_){
                ans.push_back(iterator->first);
            }
        }
        return ans;
    }
};
