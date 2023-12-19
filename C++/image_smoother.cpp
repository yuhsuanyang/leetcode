// no. 661
#include <vector>
using namespace std;
class Solution {
public:
  vector<vector<int>> imageSmoother(vector<vector<int>> &img) {
    int n_rows = img.size();
    int n_cols = img[0].size();
    vector<vector<int>> ans;
    for (int i = 0; i < n_rows; i++) {
      vector<int> row;
      for (int j = 0; j < n_cols; j++) {
        int sum = img[i][j];
        int counter = 1;
        for (int k = -1; k < 2; k++) {
          if (k == 0) {
            continue;
          }
          if ((j + k >= 0) & (j + k < n_cols)) {
            sum += img[i][j + k];
            counter++;
            if ((i + k >= 0) & (i + k < n_rows)) {
              sum += img[i + k][j + k];
              counter++;
            }
          }
          if ((i - k >= 0) & (i - k < n_rows)) {
            sum += img[i - k][j];
            counter++;
            if ((j + k >= 0) & (j + k < n_cols)) {
              sum += img[i - k][j + k];
              counter++;
            }
          }
        }
        row.push_back(sum / counter);
      }
      ans.push_back(row);
    }
    return ans;
  }
};
