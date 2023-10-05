//no. 119
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0){
            return vector<int> {1};
        }else if(rowIndex == 1){
            return vector<int> {1, 1};
        }
        vector<int> row = {1};
        vector<int> lastRow = getRow(rowIndex - 1);
        for (int i = 0;i < lastRow.size() - 1; i++){
            row.push_back(lastRow[i] + lastRow[i+1]);
        }
        row.push_back(1);
        return row;
    }
};
