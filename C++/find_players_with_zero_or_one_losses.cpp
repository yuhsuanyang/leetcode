// no. 2225
#include <vector>
using namespace std;

class Solution {
public:
  vector<vector<int>> findWinners(vector<vector<int>> &matches) {
    int lose_dict[100000] = {};
    for (vector<int> match : matches) {
      int winner = match[0] - 1;
      int loser = match[1] - 1;
      if (lose_dict[winner] == 0) {
        lose_dict[winner] = -1;
      }
      if (lose_dict[loser] == -1) {
        lose_dict[loser] = 1;
      } else {
        lose_dict[loser]++;
      }
    }
    vector<int> all_win;
    vector<int> lose_once;
    vector<vector<int>> ans;
    for (int i = 0; i < 100000; i++) {
      if (lose_dict[i] == 1) {
        lose_once.push_back(i + 1);
      } else if (lose_dict[i] == -1) {
        all_win.push_back(i + 1);
      }
    }
    ans.push_back(all_win);
    ans.push_back(lose_once);
    return ans;
  }
};
