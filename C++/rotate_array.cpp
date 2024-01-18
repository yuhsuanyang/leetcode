// no. 189
#include <vector>
using namespace std;
class Solution {
public:
  void rotate(vector<int> &nums, int k) {
    int optimize_step = k % nums.size();
    int split_point = nums.size() - optimize_step;
    vector<int> new_nums;
    for (int i = 0; i < nums.size(); i++) {
      if (i + split_point < nums.size()) {
        new_nums.push_back(nums[i + split_point]);
      } else {
        new_nums.push_back(nums[i + split_point - nums.size()]);
      }
    }
    for (int i = 0; i < nums.size(); i++) {
      nums[i] = new_nums[i];
    }
  }
};
