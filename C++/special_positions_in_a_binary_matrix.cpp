// no. 1582
#include <map>
using namespace std;
class Solution {
public:
  int numSpecial(vector<vector<int>> &mat) {
    int ans = 0;
    int n_rows = mat.size();
    int n_cols = mat[0].size();
    map<int, int> row_map;
    map<int, int> col_map;
    vector<int> one_row;
    vector<int> one_col;
    for (int i = 0; i < n_rows; i++) {
      for (int j = 0; j < n_cols; j++) {
        if (mat[i][j]) {
          one_row.push_back(i);
          one_col.push_back(j);
          row_map[i]++;
          col_map[j]++;
        }
      }
    }
    for (int i = 0; i < one_row.size(); i++) {
      if ((row_map[one_row[i]] == 1) & (col_map[one_col[i]] == 1)) {
        ans++;
      }
    }
    return ans;
  }
};
