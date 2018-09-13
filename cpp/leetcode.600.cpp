#include <bits/stdc++.h>

using namespace std;

#define LL long long

int dp[65][4];
int nums[65];

LL dfs(int pos, int status, bool flag) {
	if (pos == -1) {
		return 1;
	}
	if (!flag && dp[pos][status] != -1) {
		return dp[pos][status];
	}
	LL ans = 0;
	int e = flag ? nums[pos] : 1; // 如果flag为true就是不自由的，end只能取到nums[pos]
	for (int i = 0; i <= e; i++)
	{
//	    printf("pos %d, e %d\n", pos, e);
        if (status == 1 && i == 1) {
            continue;
        }
		int newstatus = (i == 1);
		ans += dfs(pos - 1, newstatus, flag && (i == e));
	}
	if (!flag)
	{
		dp[pos][status] = ans;
	}
	return ans;
}

LL solve(int x){
	memset(nums, 0, sizeof nums);
	memset(dp, -1, sizeof dp);
	int ppos = 0;
	while (x != 0) {
		nums[ppos++] = x % 2;
		x /= 2;
	}
//	for(int i = 0; i < ppos; i++){
//        printf("%d", nums[i]);
//	}
//	puts("");
	LL ans = dfs(ppos - 1, 0, 1);
	return ans;
}

class Solution {
public:
    int findIntegers(int num) {
        return solve(num);
    }
};

//int main()
//{
//    Solution sln;
//    printf("%d\n", sln.findIntegers(5));
//    return 0;
//}
