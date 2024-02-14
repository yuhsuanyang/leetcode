// no. 2149
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> rearrangeArray(vector<int> &nums) {
    vector<int> pos_part;
    vector<int> neg_part;
    for (int i : nums) {
      if (i < 0) {
        neg_part.push_back(i);
      } else {
        pos_part.push_back(i);
      }
    }
    for (int i = 0; i < nums.size(); i++) {
      if (i % 2) {
        nums[i] = neg_part[i / 2];
      } else {
        nums[i] = pos_part[i / 2];
      }
    }
    return nums;
  }
};
