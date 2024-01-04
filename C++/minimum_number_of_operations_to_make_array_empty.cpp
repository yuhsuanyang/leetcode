// no. 2870
#include <map>
#include <vector>
using namespace std;
class Solution {
public:
  int getMinDeletion(int num) {
    if (num <= 3) {
      return 1;
    }
    int total_deletion = 0;
    int num_deletion = 0;
    while (num > 4) {
      if (num % 3 == 1) {
        num_deletion = num / 3 - 1;
      } else {
        num_deletion = num / 3;
      }
      num -= num_deletion * 3;
      total_deletion += num_deletion;
    }
    num_deletion = num / 2;
    total_deletion += num_deletion;
    return total_deletion;
  }
  int minOperations(vector<int> &nums) {
    int ans = 0;
    map<int, int> num_counts;
    for (int i = 0; i < nums.size(); i++) {
      num_counts[nums[i]]++;
    }
    for (map<int, int>::iterator it = num_counts.begin();
         it != num_counts.end(); it++) {
      if (it->second == 1) {
        return -1;
      }
      ans += getMinDeletion(it->second);
    }
    return ans;
  }
};
