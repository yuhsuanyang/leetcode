// no. 8
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int myAtoi(string s) {
    int ans = 0;
    vector<char> nums;
    int sign = 1;
    int start = 0;
    int upper_bound = pow(2, 31) - 1;
    int lower_bound = (-1) * pow(2, 31);
    for (int i = 0; i < s.length(); i++) {
      if (s[i] != ' ') {
        start = i;
        break;
      }
    }
    for (int i = start; i < s.length(); i++) {
      if ((int(s[i]) <= 57) & (int(s[i]) >= 48)) {
        nums.push_back(s[i]);
      } else if ((s[i] == '-') | (s[i] == '+')) {
        if (nums.empty()) {
          nums.push_back(s[i]);
        } else {
          break;
        }
      } else {
        break;
      }
    }
    if (nums.empty()) {
      return 0;
    }
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == '-') {
        sign = (-1);
        continue;
      } else if (nums[i] == '+') {
        continue;
      }
      int digit = int(nums[i]) - 48;
      if ((ans > upper_bound / 10) | (ans == upper_bound / 10) & digit > 7) {
        if (sign == 1) {
          return upper_bound;
        } else {
          return lower_bound;
        }
      }
      ans = ans * 10 + digit;
    }
    return sign * ans;
  }
};
