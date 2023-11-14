//no. 1930
#include <string>
#include <set>
#include <map>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        map <char, vector<int> > counter;
        for(int i = 0; i < s.length(); i++){
            counter[s[i]].push_back(i);
        }
        set<char> pan;
        int ans = 0;
        for(map<char, vector<int> >::iterator it = counter.begin(); it != counter.end(); it++){         
            pan.clear();
            char head = it->first;
            int start = it->second[0] + 1;
            int end = it->second.back();
            for (int i = start; i < end; i++){
                pan.insert(s[i]);
            }
            ans += pan.size();
        }
        return ans;
    }
};
