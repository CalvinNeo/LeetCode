
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

char dp[2020][2020];

class Solution {
public:
    bool dfs(vector<int>& stones, int i, int k){
        int n = stones.size();
        if(dp[i][k] != -1){
            return dp[i][k];
        }
        if(i == n - 1){
            return true;            
        }
        int pos = stones[i];
        bool ans = false;
        for(int d = k - 1; d <= k + 1; d++){
            if(d > 0){
                int new_pos = pos + d;
                auto iter = lower_bound(stones.begin(), stones.end(), new_pos);
                int index = iter - stones.begin();
                if(iter != stones.end() && stones[index] == new_pos){
                    ans = ans || dfs(stones, index, d);
                }
            }
        }
        dp[i][k] = ans;
        return ans;
    }
    bool canCross(vector<int>& stones) {
        int n = stones.size();
        memset(dp, -1, sizeof dp);
        if (n == 1){
            return true;
        }
        else{
            if (stones[1] - stones[0] == 1){
                return dfs(stones, 1, 1);
            } 
            else{
                return false;
            } 
        }
    }
};

int main(){
    Solution sln;
    vector<int> vec ;
    vec = {0,1,2,3,4,8,9,11};
    vec = {0,1,3,5,6,8,12,17};
    printf("%s\n", sln.canCross(vec) ? "true": "false");
}