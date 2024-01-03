// no. 2125
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int countLights(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] == '1') {
        count++;
      }
    }
    return count;
  }
  int numberOfBeams(vector<string> &bank) {
    int ans = 0;
    int top = 0;
    int down = 0;
    for (int i = 0; i < bank.size(); i++) {
      int n_row_lights = countLights(bank[i]);
      if (n_row_lights) {
        if (top == 0) {
          top = n_row_lights;
        } else if (down == 0) {
          down = n_row_lights;
          ans += down * top;
          top = down;
          down = 0;
        }
      }
    }
    return ans;
  }
};
