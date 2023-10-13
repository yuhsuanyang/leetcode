// no.343
#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Solution {
    public:
        map <int, vector<int> > best_sum;
        Solution(){
            best_sum[1].push_back(1);
            best_sum[2].push_back(1);
            best_sum[2].push_back(1);
        }
        vector<vector<int> > decompose(vector<int> v){
            vector<vector<int> >result;
            for (int i = 0; i < v.size(); i++){
                vector<int> r;
                int end = max(0, i - 2);
                r.insert(r.end(), v.begin(), v.begin() + end);
                r.insert(r.end(), best_sum[v[i]].begin(), best_sum[v[i]].end());
                r.insert(r.end(), v.begin() + i + 1, v.end());
                result.push_back(r);
                }
            return result;
            }

        int product(vector<int> v){
            int result = 1;
            for (int i = 0; i < v.size(); i++){
                result *= v[i];
            }
            return result;
        }

        int integerBreak(int n) {
            if (n == 2){
                return 1;
            }
            for (int i = 3; i <= n; i++){
                vector<int> last_state = best_sum[i - 1];
                int max_product = 1;
                vector<int> selected;
                for (int j = 0; j < last_state.size(); j++){
                    vector<int> candidate = last_state;
                    candidate[j] += 1;
                    int p = product(candidate);
                    if (p > max_product){
                        max_product = p;
                        selected = candidate;
                        vector<vector<int> > decomposed_candidate = decompose(candidate);
                        for (int k=0; k < decomposed_candidate.size(); k++){
                            int p = product(decomposed_candidate[k]);
                            if(p >= max_product){
                                selected = decomposed_candidate[k];
                                max_product = p;
                            }
                        }
                    }
                }
                best_sum[i] = selected;
            }
        return product(best_sum[n]);
    }
    void print_best_sum(){
        for(map<int, vector<int> >::iterator it = best_sum.begin(); it != best_sum.end(); it++){
            cout << it->first << ": ";
            print_vector(it->second);
            cout << endl;
        }

    }
    void print_vector(vector<int> v){
        cout << "[";
        for(int i = 0; i < v.size(); i++){
            cout << v[i] << " ";
        }
        cout << "]" << endl;
    }
};

int main(){
    Solution sol;
    cout << sol.integerBreak(58) << endl;
    sol.print_best_sum();
    return 1;
}
