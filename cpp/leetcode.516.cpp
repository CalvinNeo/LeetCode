#include <bits/stdc++.h>

using namespace std;
#define LL long long

int dp[1010][1010];

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        memset(dp, 0, sizeof dp);
        int n = s.size();
        if(n <= 1)
            return n;
        else if(n == 2)
            return s[0] == s[1] ? 2 : 1;
        int flag = 0;
        for(int i = 0; i < n; i++){
            if(s[i] == s[n - 1])
                flag = 1;
            if(flag)
                dp[i][n - 1] = 2;
        }
        flag = 0;
        for(int i = n - 1; i > 0; i--){
            if(s[i] == s[0])
                flag = 1;
            if(flag)
                dp[0][i] = 2;
        }

        for(int i = 0; i < n; i++){
            for(int j = n - 1; j > i; j--){
                if(s[i] == s[j] && i - 1 >= 0 && j + 1 < n){
                    dp[i][j] = max(dp[i - 1][j + 1] + 2, dp[i][j]);
                }
                if(i - 1 >= 0){
                    dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                }
                if(j + 1 < n){
                    dp[i][j] = max(dp[i][j], dp[i][j + 1]);
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < n - 1; i++){
            if(i + 2 < n)
                ans = max(dp[i][i + 2] + 1, ans);
            ans = max(dp[i][i + 1], ans);
        }
        return ans;
    }
};