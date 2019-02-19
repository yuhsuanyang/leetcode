#include <iostream> 
#include <algorithm>    
#include <vector>
#include <iterator>   
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	vector<int> y;
        for(int i=0;i<nums.size();i++){
            int x=target-nums[i];
            vector<int>::iterator r;
            
            r=find(nums.begin()+i+1, nums.end(), x); 
            if (r != nums.end()){
            	int z=distance(nums.begin(),r); //計算r在nums裡面和nums.begin()之間隔了多少個element
            	y.push_back(i);
           		y.push_back(z);
           		cout<<"finish at "<<i<<endl;
           		break;
			}
           
        }
        return y;
   }
};
int main(){
	int array[] = {2,5,5,11};
	vector <int> vec,ans;
	vec.assign(array, array+4);
	for(int i=0;i<vec.size();i++){
		cout<<vec[i]<<' ';
	};
	vector<int>::iterator it;
	it = find (vec.begin(), vec.end(), 10); //find if 10 is in vec
	if (it != vec.end()){  //vec.end() 回傳一個 iterator，它指向 vector 最尾端元素的下一個位置
		cout<< *it<<endl;
	}else{
		cout<<"not found"<<endl;
	};
	Solution s;
	ans=s.twoSum(vec,10);
	for(int i=0;i<ans.size();i++){
		cout<<ans[i]<<' '; 
	} 
	return 0;
	
};
//iterator is a kind of pointer

