// no.1441
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> actions;
        int i = 1;
        int j = 0;
        while(i <= n & j < target.size()){
            actions.push_back("Push");
            if (target[j] != i){
                actions.push_back("Pop");
            }else{
                j++;
            }
            i++;
        }
        return actions;
    }
};
