// no.5
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string longestPalindrome(string s) {
    int n = s.length();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    string ans = "";
    for (int diff = 0; diff < n; diff++) {
      for (int i = 0; i < n - diff; i++) {
        int j = i + diff;
        if (s[i] == s[j]) {
          if (diff <= 1) {
            dp[i][j] = true;
            ans = s.substr(i, diff + 1);

          } else {
            if (dp[i + 1][j - 1]) {
              dp[i][j] = true;
              ans = s.substr(i, diff + 1);
            }
          }
        }
      }
    }
    return ans;
  }
};
