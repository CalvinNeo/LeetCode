#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <functional> 
#include <algorithm> 
#include <vector>

using namespace std;

#define inf 0x3f3f3f3f

int alphabeta_dfs(int sgn, vector<int> & nums, int l, int r, int & alpha, int & beta){
    if(l == r){
        return nums[l];
    }
    int child_alpha = alpha, child_beta = beta;
    int lnd = alphabeta_dfs(-sgn, nums, l + 1, r, child_alpha, child_beta);
    int ansl = lnd + sgn * nums[l];
    alpha = max(alpha, child_alpha);
    beta = min(beta, child_beta);
    if(beta >= alpha){
        int rnd = alphabeta_dfs(-sgn, nums, l, r - 1, child_alpha, child_beta);
        int ansr = rnd + sgn * nums[r];
        alpha = max(alpha, child_alpha);
        beta = min(beta, child_beta);
        return sgn > 0 ? max(ansl, ansr) : min(ansl, ansr);
    }else{
        return ansl;
    }
}

class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        int child_alpha = -inf, child_beta = inf;
        return alphabeta_dfs(1, nums, 0, n - 1, child_alpha, child_beta) >= 0;
    }
};