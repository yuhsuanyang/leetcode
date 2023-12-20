// no.2706
#include <vector>
using namespace std;

class Solution {
public:
  int getMin(vector<int> &nums) {
    int min_index = 0;
    int min_ = nums[min_index];
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] < min_) {
        min_ = nums[i];
        min_index = i;
      }
    }
    nums.erase(nums.begin() + min_index);
    return min_;
  }
  int buyChoco(vector<int> &prices, int money) {
    int first = getMin(prices);
    if (first >= money) {
      return money;
    }
    int second = getMin(prices);
    int change = money - first - second;
    return change >= 0 ? change : money;
  }
};
