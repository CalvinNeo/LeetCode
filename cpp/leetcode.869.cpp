#include <bits/stdc++.h>

using namespace std;

int dp[20];
int len = 0;

int getv(){
    int ans = 0;
    for(int i = len - 1; i >= 0; i--){
        ans *= 10;
        ans += dp[i];
    }
    return ans;
}

class Solution {
public:
    bool reorderedPowerOf2(int N) {
        memset(dp, 0, sizeof dp);
        int x = N;
        len = 0;
        while(x){
            dp[len++] = x % 10;
            x /= 10;
        }
        sort(dp, dp + len);
//            printf("len, %d %d %d\n", len, dp[len - 1], dp[0]);
        do{
            if(dp[len - 1] == 0){
//                    puts("Hit");
                continue;
            }
            int ch = getv();
//            printf("ch %d\n", ch);
            if((ch & (ch - 1)) == 0){
                return true;
            }
        }
        while(next_permutation(dp, dp + len));
        return false;
    }
};

int main()
{
    Solution sln;
    printf("%d\n", sln.reorderedPowerOf2(0));
    printf("%d\n", sln.reorderedPowerOf2(1));
    printf("%d\n", sln.reorderedPowerOf2(2));
    printf("%d\n", sln.reorderedPowerOf2(20));
    printf("%d\n", sln.reorderedPowerOf2(10));
    printf("%d\n", sln.reorderedPowerOf2(16));
    printf("%d\n", sln.reorderedPowerOf2(24));
    return 0;
}
