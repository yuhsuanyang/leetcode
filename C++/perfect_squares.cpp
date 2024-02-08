// no. 279
#include <vector>
using namespace std;

class Solution {
public:
  int numSquares(int n) {
    if (n <= 3) {
      return n;
    }
    vector<int> squares;
    vector<int> dp;
    for (int i = 0; i <= n; i++) {
      dp.push_back(0);
    }
    for (int i = 1; i < n; i++) {
      if (i * i > n) {
        break;
      } else {
        squares.push_back(i * i);
        dp[i * i] = 1;
      }
    }
    for (int i = 1; i <= n; i++) {
      if (dp[i] == 0) {
        int min_ = dp[i - 1];
        for (int j : squares) {
          if (j > i) {
            break;
          }
          min_ = min(min_, dp[i - j]);
        }
        dp[i] = min_ + 1;
      }
    }
    return dp.back();
  }
};
