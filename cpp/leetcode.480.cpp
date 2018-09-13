#include <bits/stdc++.h>

using namespace std;

#define LL long long

multiset<int> ms;

class Solution {
public:
    double get_med(int k){
        if(k & 1){
            auto iter = ms.begin();
            iter = next(iter, k / 2);
            return *iter;
        }else{
            auto iter = ms.begin();
            iter = next(iter, (k - 1) / 2);
            LL acc = *iter;
            iter = next(iter, 1);
            acc += *iter;
            return acc / 2.0;
        }
    }
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        ms = multiset<int>(nums.begin(), nums.begin() + k);
        vector<double> ans;
        int n = nums.size();
        ans.push_back(get_med(k));
        for(int i = k; i < n; i++){
            ms.insert(nums[i]);
            ms.erase(ms.lower_bound(nums[i-k]));
            ans.push_back(get_med(k));
        }
        return ans;
    }
};

//void look_up(const vector<double> & vec){
//    for(auto x : vec){
//        printf("%f ", x);
//    }
//    puts("");
//}
//
//int main()
//{
//    Solution sln;
//    vector<int> inp;
//    inp = {1,3,-1,-3,5,3,6,7};
//    look_up(sln.medianSlidingWindow(inp, 3));
//    inp = {2147483647,2147483647};
//    look_up(sln.medianSlidingWindow(inp, 2));
//    return 0;
//}
