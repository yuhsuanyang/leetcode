// no. 1422
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int maxScore(string s) {
    int max_score = 0;
    vector<int> ones;
    for (int i = 0; i < s.length() - 1; i++) {
      if (s[i] == '1') {
        ones.push_back(i);
      }
    }
    ones.push_back(s.length() - 1);
    for (int i = 0; i < ones.size(); i++) {
      int j = ones[i];
      if (j == 0) {
        continue;
      }
      int right_score = ones.size() - i;
      if (s.back() == '0') {
        right_score--;
      }
      int left_score = j - i;
      int total = left_score + right_score;
      if (total > max_score) {
        max_score = total;
      }
    }
    return max_score;
  }
};
