// no.1578
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  int minCost(string colors, vector<int> &neededTime) {
    int cost = 0;
    int max_time = neededTime[0];
    for (int i = 1; i < neededTime.size(); i++) {
      if (colors[i] == colors[i - 1]) {
        if (neededTime[i] > max_time) {
          cost += max_time;
          max_time = neededTime[i];
        } else {
          cost += neededTime[i];
        }
      } else {
        max_time = neededTime[i];
      }
    }
    return cost;
  }
};
