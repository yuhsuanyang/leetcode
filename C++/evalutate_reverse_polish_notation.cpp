// no. 150
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> stack;
  vector<int> get_operate_nums() {
    int num1 = stack.back();
    stack.pop_back();
    int num2 = stack.back();
    stack.pop_back();
    vector<int> nums = {num1, num2};
    return nums;
  }
  int evalRPN(vector<string> &tokens) {
    for (string i : tokens) {
      if (i == "+") {
        vector<int> nums = get_operate_nums();
        stack.push_back(nums[0] + nums[1]);
      } else if (i == "-") {
        vector<int> nums = get_operate_nums();
        stack.push_back(nums[1] - nums[0]);
      } else if (i == "*") {
        vector<int> nums = get_operate_nums();
        stack.push_back(nums[0] * nums[1]);
      } else if (i == "/") {
        vector<int> nums = get_operate_nums();
        stack.push_back(nums[1] / nums[0]);
      } else {
        stack.push_back(stoi(i));
      }
    }
    return stack[0];
  }
};
