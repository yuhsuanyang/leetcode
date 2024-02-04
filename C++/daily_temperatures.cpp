// no. 739
#include <vector>
using namespace std;
class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    vector<int> stack;
    vector<int> answer;
    for (int i = 0; i < temperatures.size(); i++) {
      answer.push_back(0);
    }
    for (int i = 0; i < temperatures.size(); i++) {
      if (stack.empty()) {
        stack.push_back(i);
      } else {
        int j = 0;
        while ((temperatures[stack.back()] < temperatures[i])) {
          j = stack.back();
          stack.pop_back();
          answer[j] = i - j;
          if (stack.empty()) {
            break;
          }
        }
        stack.push_back(i);
      }
    }
    return answer;
  }
};
