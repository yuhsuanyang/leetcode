// no. 55
#include <vector>
using namespace std;

class Solution {
public:
  bool canJump(vector<int> &nums) {
    vector<bool> appoarchable;
    for (int i = 0; i < nums.size(); i++) {
      appoarchable.push_back(false);
    }
    appoarchable[0] = true;
    for (int i = 0; i < nums.size(); i++) {
      if (appoarchable.back()) {
        return true;
      }
      if (appoarchable[i]) {
        for (int k = i + 1; k < nums[i] + i + 1; k++) {
          if (k >= nums.size()) {
            break;
          }
          if (!appoarchable.back()) {
            appoarchable[k] = true;
          }
        }
      }
    }
    return appoarchable.back();
  }
};
