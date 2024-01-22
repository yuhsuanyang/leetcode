// no. 198
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
  int rob(vector<int> &nums) {
    if (nums.size() == 1) {
      return nums[0];
    }
    vector<int> dp;
    dp.push_back(nums[0]);
    dp.push_back(nums[1]);
    for (int i = 2; i < nums.size(); i++) {
      if (i == 2) {
        dp.push_back(dp[0] + nums[i]);
      } else {
        dp.push_back(max(dp[i - 2], dp[i - 3]) + nums[i]);
      }
    }
    return max(dp[nums.size() - 2], dp[nums.size() - 1]);
  }
};
