// no. 42
#include <vector>
using namespace std;
class Solution {
public:
  int trap(vector<int> &height) {
    vector<int> stack;
    stack.push_back(0);
    int ans = 0;
    for (int i = 0; i < height.size(); i++) {
      while (height[i] > height[stack.back()]) {
        if (stack.size() >= 2) {
          int h = min(height[stack[stack.size() - 2]], height[i]) -
                  height[stack.back()];
          int w = (i - stack[stack.size() - 2] - 1);
          ans += h * w;
        }
        stack.pop_back();
        if (stack.empty()) {
          break;
        }
      }
      stack.push_back(i);
    }
    return ans;
  }
};
