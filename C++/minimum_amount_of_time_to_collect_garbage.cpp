//no.2391
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    int calculate_time(vector<int>& sort_of_garbage, vector<int>& travel){
        int garbage_count = sort_of_garbage.size();
        if(garbage_count){
            int start = 0;
            int end = sort_of_garbage[sort_of_garbage.size() - 1];
            for(int i = start; i < end; i++){
                garbage_count += travel[i];
            }
            return garbage_count;
        }else{
            return 0;
        }
    }
    int garbageCollection(vector<string>& garbage, vector<int>& travel) {
        vector<int> glass, metal, paper;
        for(int i = 0; i < garbage.size(); i++){
            for(int j = 0; j < garbage[i].size(); j++){
                if (garbage[i][j] == 'G'){
                    glass.push_back(i);
                }
                if (garbage[i][j] == 'M'){
                    metal.push_back(i);
                }
                if (garbage[i][j] == 'P'){
                    paper.push_back(i);
                }
            }
        }
        int glass_time = calculate_time(glass, travel);
        int metal_time = calculate_time(metal, travel);
        int paper_time = calculate_time(paper, travel);
        return glass_time + metal_time + paper_time;
    }
};
