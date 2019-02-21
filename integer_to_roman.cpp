#include <iostream>
#include <string>
#include <map>
using namespace std;
//在C++中字串的本質是由字元所組成的陣列，並在最後加上一個空（null）字元'\0'

class Solution {
public:
	map<int, string>m[4];
	Solution(){
		m[0][1]="M";
		m[1][1]="C";
		m[2][1]="X";
		m[3][1]="I";
		m[1][5]="D";
		m[2][5]="L";
		m[3][5]="V";
		for(int i=0;i<4;i++){
			m[i][0]="";
			if(i!=0){
				m[i][4]=m[i][1]+m[i][5];
				m[i][9]=m[i][1]+m[i-1][1];
			}
		}
	}
    string intToRoman(int num) {
    	int result[4];
		int tens[4]={1000,100,10,1};
		string ans="";
		for(int i=0;i<4;i++){
			result[i]=num/tens[i];
			num=num-tens[i]*result[i];
		};
		for(int i=0;i<4;i++){
			//cout<<result[i]<<" ";
			if(result[i]==0 or result[i]==4 or result[i]==9){
				ans=ans+m[i][result[i]];
			}else{
				if(result[i]>=5){
					ans=ans+m[i][5];
				};
				for(int j=0;j<result[i]%5;j++){
					ans=ans+m[i][1];
				}
			}
		};
        return ans;
    };
};
int main(){
	Solution sol;
	//cout<<sol.m[3][5]<<endl;
	cout<<sol.intToRoman(1994)<<endl;
	return 0;
}
