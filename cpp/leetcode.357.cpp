#include <bits/stdc++.h>

int dp[1000][4096];
int nums[1000];

bool geti(int x, int i){
    return (x >> i) & 1;
}

int seti(int x, int i, bool v){
    if(v){
        return x | (1 << i);
    }else{
        return x & (~(1 << i));
    }
}

class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        int ppos = 0;
        memset(nums, 0, sizeof nums);
        memset(dp, -1, sizeof dp);
        if(n == 0){
            return 1;
        }
        while(n-- > 0){
            nums[ppos++] = 9;
        }
        std::function<int(int, int, bool)> dfs = [&](int pos, int status, bool flag) -> int{
            if (pos == -1)
            {
                return !geti(status, 10);
            }
            if(!flag && dp[pos][status] != -1){
                return dp[pos][status];
            }
            int ans = 0;
            int end = flag ? nums[pos] : 9;
            for(int i = 0; i <= end; i++){
                int newstatus = status;
                bool repeated = false;
                
                if(i >= 1 && i <= 9){
                    newstatus = seti(newstatus, 11, 1);
                }
                
                if(geti(newstatus, 11)){
                    // If this zero is not leading zero
                    repeated = geti(status, i);
                    newstatus = seti(newstatus, i, 1);          
                    if(repeated){
                        newstatus = seti(newstatus, 10, repeated);
                    }
                }
                
                bool newflag = flag && (i == end); 
                ans += dfs(pos - 1, newstatus, newflag);
            }
            if(!flag && dp[pos][status] == -1){
                dp[pos][status] = ans;
            }
            return ans;
        };
        int ans = dfs(ppos - 1, 0, true);
        return ans;
    }
};

int main(){
    Solution sln;
//  printf("%d\n", geti(2, 1));
//  printf("%d\n", geti(2, 0));
//  printf("%d\n", seti(2, 0, 1));
//  printf("%d\n", seti(4, 0, 1));
//  printf("%d\n", seti(4, 1, 1));
    printf("%d\n", sln.countNumbersWithUniqueDigits(0));
    printf("%d\n", sln.countNumbersWithUniqueDigits(1));
    printf("%d\n", sln.countNumbersWithUniqueDigits(2));
}