// no. 1436
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  string destCity(vector<vector<string>> &paths) {
    vector<vector<string>> route;
    route.push_back(paths[0]);
    paths.erase(paths.begin());
    while (paths.size()) {
      for (int i = 0; i < paths.size(); i++) {
        if (paths[i][0] == route.back()[1]) {
          route.push_back(paths[i]);
          paths.erase(paths.begin() + i);
          break;
        }
      }
      for (int i = 0; i < paths.size(); i++) {
        if (paths[i][1] == route.front()[0]) {
          route.insert(route.begin(), paths[i]);
          paths.erase(paths.begin() + i);
          break;
        }
      }
    }
    return route.back()[1];
  }
};
