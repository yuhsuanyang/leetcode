// no. 931
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  int minFallingPathSum(vector<vector<int>> &matrix) {
    int n = matrix.size();
    vector<vector<int>> dp;
    for (int i = 0; i < n - 1; i++) {
      vector<int> row;
      dp.push_back(row);
    }
    dp.push_back(matrix.back());
    for (int row = n - 2; row > -1; row--) {
      for (int col = 0; col < n; col++) {
        int min_;
        if (col == 0) {
          min_ = min(dp[row + 1][col], dp[row + 1][col + 1]);
        } else if (col == n - 1) {
          min_ = min(dp[row + 1][col], dp[row + 1][col - 1]);
        } else {
          min_ = min(dp[row + 1][col], dp[row + 1][col + 1]);
          min_ = min(min_, dp[row + 1][col - 1]);
        }
        dp[row].push_back(matrix[row][col] + min_);
      }
    }
    int ans = dp[0][0];
    for (int i = 0; i < n; i++) {
      if (dp[0][i] < ans) {
        ans = dp[0][i];
      }
    }
    return ans;
  }
};
