#include <bits/stdc++.h>

using namespace std;

map<int, set<int>> mp;

class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        mp = map<int, set<int>>();
        int acc = 0;
        mp[0] = {-1};
        int mx = 0;

        for(int i = 0; i < n; i++){
            int delta = nums[i] == 0 ? -1 : 1;
            acc += delta;

            map<int, set<int>>::iterator iter = mp.find(acc);
            if (iter != mp.end()){
                mx = max(mx, i - *(iter->second.begin()) );
            }

            if (iter == mp.end()){
                mp[acc] = set<int>();
            }
            mp[acc].insert(i);
        }
        return mx;
    }
};

//int main()
//{
//    Solution sln;
//    vector<int> inp;
//    inp = {0, 1};
//    printf("%d\n", sln.findMaxLength(inp));
//    inp = {0, 1, 0};
//    printf("%d\n", sln.findMaxLength(inp));
//    inp = {0, 1, 1};
//    printf("%d\n", sln.findMaxLength(inp));
//    return 0;
//}
