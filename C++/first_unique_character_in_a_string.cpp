// no. 387
#include <map>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int firstUniqChar(string s) {
    map<char, vector<int>> counter;
    for (int i = 0; i < s.length(); i++) {
      counter[s[i]].push_back(i);
    }
    int first_index = s.length();
    map<char, vector<int>>::iterator it;
    for (it = counter.begin(); it != counter.end(); it++) {
      if ((it->second.size() == 1) & (it->second[0] < first_index)) {
        first_index = it->second[0];
      }
    }
    return first_index == s.length() ? -1 : first_index;
  }
};
