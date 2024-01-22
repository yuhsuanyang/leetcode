// no. 645
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> findErrorNums(vector<int> &nums) {
    map<int, int> counter;
    vector<int> ans = {0, 0};
    int n = nums.size();
    for (int i : nums) {
      counter[i]++;
    }
    for (int i = 1; i < n + 1; i++) {
      map<int, int>::iterator it = counter.find(i);
      if (it->second == 2) {
        ans[0] = i;
      } else if (it == counter.end()) {
        ans[1] = i;
      }
    }
    return ans;
  }
};
