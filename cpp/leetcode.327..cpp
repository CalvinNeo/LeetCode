#include <bits/stdc++.h>
#include <vector>

using namespace std;

#define LL long long

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        // 这个类似560的做法就会T了
        LL acc = 0;
        int n = nums.size();
        map<LL, int> st;
        int ans = 0;
        st[0] = 1;
        for(int i = 0; i < n; i++){
            acc += nums[i];
            LL w_least = acc - upper;
            LL w_most = acc - lower;
            auto b = st.lower_bound(w_least);
            auto e = st.upper_bound(w_most);
            for(; b != e; b++){
                ans += (*b).second;
            }
            map<LL, int>::iterator iter = st.find(acc);
            if (iter == st.end()){
                st[acc] = 0;
            }
            st[acc] ++;
        }
        return ans;
    }
};

//int main()
//{
//    Solution sln;
//    vector<int> inp;
//    inp = {-2, 5, -1};
//    printf("%d\n", sln.countRangeSum(inp, -2, 2));
//    inp = {-2147483647,0,-2147483647,2147483647};
//    printf("%d\n", sln.countRangeSum(inp, -564, 3864));
//    return 0;
//}
