// no. 2610
#include <map>
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> findMatrix(vector<int> &nums) {
    vector<vector<int>> ans = {};
    map<int, int> curr_row;
    for (int i = 0; i < nums.size(); i++) {
      int row = curr_row[nums[i]];
      int n_rows = ans.size();
      if (row > n_rows - 1) {
        vector<int> new_row;
        new_row.push_back(nums[i]);
        ans.push_back(new_row);
      } else {
        ans[row].push_back(nums[i]);
      }
      curr_row[nums[i]] = row + 1;
    }
    return ans;
  }
};
