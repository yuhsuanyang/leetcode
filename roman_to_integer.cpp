#include <iostream>
#include <string.h>
#include <vector>
using namespace std;
class Roman{
	public:
		Roman(char c){
			input=c;
		};
		int get_value(){
			int value;
			switch(input){
				case 'I':
					value=1;
					break;
				case 'V':
					value=5;
					break;
				case 'X':
					value=10;
					break;
				case 'L':
					value=50;
					break;
				case 'C':
					value=100;
					break;
				case 'D':
					value=500;
					break;
				case 'M':
					value=1000;
					break;
			};
			return value;
		};
	private:
		char input;
};
class Solution {
public:
    int romanToInt(string s) {
        vector<char>arr;
        for(int i=0;i<s.size();i++){
        	arr.push_back(s[i]);
        	//cout<<arr[i]<<endl;
		};
		int j=0;
		int ans=0;
		while(j<s.size()){
			Roman a(arr[j]);
			int r;
			if(IXC(arr,j)==1){
				Roman b(arr[j+1]);
				r=b.get_value()-a.get_value();
				j=j+2;
			}else{
				r=a.get_value();
				j=j+1;
			}
			cout<<r<<endl;
			ans=ans+r;
		};
		cout<<ans<<endl;
		return ans;
    };
    bool IXC(vector<char> & num,int i){
    	if(i==num.size()-1){
    		return 0;
		};
    	switch(num[i]){
    		case 'I':
    			if (num[i+1]=='V' or num[i+1]=='X'){
    				return 1;
				}else{
					return 0;
				};
			case 'X':
				if (num[i+1]=='L' or num[i+1]=='C'){
    				return 1;
				}else{
					return 0;
				};
			case 'C':
				if (num[i+1]=='D' or num[i+1]=='M'){
    				return 1;
				}else{
					return 0;
				};
			default:
				return 0;
		};	
	};
};

int main(){
	Solution sol;
	sol.romanToInt("MCDLXXVI");
	return 0;
} 
