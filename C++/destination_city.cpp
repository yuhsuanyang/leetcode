// no. 1436
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string destCity(vector<vector<string>> &paths) {
    string start = paths[0][0];
    string end = paths[0][1];
    paths.erase(paths.begin());
    while (paths.size()) {
      for (int i = 0; i < paths.size(); i++) {
        if (paths[i][0] == end) {
          end = paths[i][1];
          paths.erase(paths.begin() + i);
          break;
        }
      }
      for (int i = 0; i < paths.size(); i++) {
        if (paths[i][1] == start) {
          start = paths[i][0];
          paths.erase(paths.begin() + i);
          break;
        }
      }
    }
    return end;
  }
};
