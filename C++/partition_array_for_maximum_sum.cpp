// no. 1043
#include <vector>
using namespace std;

class Solution {
public:
  int maxSumAfterPartitioning(vector<int> &arr, int k) {
    int n = arr.size();
    vector<int> dp;
    for (int i = 0; i < n; i++) {
      dp.push_back(0);
    }
    dp[n - 1] = arr[n - 1];
    dp.push_back(0);
    for (int start = n - 2; start >= 0; start--) {
      int curr_max = 0;
      int end = min(start + k, n);
      for (int i = start; i < end; i++) {
        curr_max = max(arr[i], curr_max);
        dp[start] = max(dp[start], dp[i + 1] + curr_max * (i - start + 1));
      }
    }
    return dp[0];
  }
};
