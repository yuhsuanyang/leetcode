// no. 1759
#include <string>
using namespace std;

class Solution {
public:
    int countHomogenous(string s) {
        int ans = 1;
        int curr_streak = 1;
        int mod = 1e9 + 7;
        for(int i = 0; i < s.length() - 1; i++){
            if(s[i] == s[i + 1]){
                curr_streak ++;
            }else{
                curr_streak = 1;
            }
            ans += curr_streak;
            ans = ans % mod;
        }
        return ans;
    }
};
