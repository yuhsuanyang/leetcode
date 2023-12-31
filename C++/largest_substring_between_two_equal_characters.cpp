// no. 1624
#include <string>
using namespace std;
class Solution {
public:
  int maxLengthBetweenEqualCharacters(string s) {
    int ans = -1;
    for (int i = 0; i < s.length(); i++) {
      for (int j = s.length() - 1; j > 0; j--) {
        if (s[j] == s[i]) {
          int length_between_equal = j - i - 1;
          if (length_between_equal > ans) {
            ans = length_between_equal;
          }
          break;
        }
      }
    }
    return ans;
  }
};
