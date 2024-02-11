// no. 647
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  int countSubstrings(string s) {
    int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    int ans = 0;
    for (int diff = 0; diff < n; diff++) {
      for (int i = 0; i < n - diff; i++) {
        int j = i + diff;
        if (s[i] == s[j]) {
          if (diff <= 1) {
            dp[i][j] = true;
            ans++;
          } else {
            if (dp[i + 1][j - 1]) {
              dp[i][j] = true;
              ans++;
            }
          }
        }
      }
    }
    return ans;
  }
};
