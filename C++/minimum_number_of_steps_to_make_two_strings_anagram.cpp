// no. 1347
#include <map>
#include <string>
using namespace std;

class Solution {
public:
  int minSteps(string s, string t) {
    int length = s.length();
    map<char, int> move_map;
    for (int i = 0; i < length; i++) {
      move_map[s[i]]++;
      move_map[t[i]]--;
    }
    int ans = 0;
    for (map<char, int>::iterator it = move_map.begin(); it != move_map.end();
         it++) {
      if (it->second > 0) {
        ans += it->second;
      }
    }
    return ans;
  }
};
