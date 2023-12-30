// no. 1897
#include <map>
#include <string>
using namespace std;

class Solution {
public:
  bool makeEqual(vector<string> &words) {
    map<char, int> char_map;
    for (int i = 0; i < words.size(); i++) {
      for (int j = 0; j < words[i].length(); j++) {
        char_map[words[i][j]]++;
      }
    }
    for (map<char, int>::iterator it = char_map.begin(); it != char_map.end();
         it++) {
      if (it->second % words.size()) {
        return false;
      }
    }
    return true;
  }
};
