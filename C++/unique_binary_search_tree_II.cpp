//no. 95
#include <iostream>
#include <vector>
#include "tree_node.h"
using namespace std;

class Solution {
    public:
        vector<TreeNode*> generateTrees(int n) {
            return getTrees(1, n);            
        }
        vector <TreeNode*> getTrees(int start, int end){
            vector<TreeNode*> result;
            if (start > end){
                result.push_back(NULL);
                return result;
            }else if(start == end){
                result.push_back(new TreeNode(start));
                return result;
            }
            for(int root=start; root <= end; root ++){
                vector<TreeNode*> lefts = getTrees(start, root-1);
                vector<TreeNode*> rights = getTrees(root+1, end);
                for(int i = 0; i < lefts.size(); i++){
                    for(int j = 0; j < rights.size(); j++){
                        result.push_back(new TreeNode(root, lefts[i], rights[j]));
                    }
                }
            }
            return result;
        }

};

int main(){
    Solution sol;
    for (int i = 0; i <= 8; i++){
        vector<TreeNode*> ans = sol.generateTrees(i);
        cout << i << " " << ans.size() << endl;
        cout << "--------" << endl;
    }
}
