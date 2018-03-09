#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <cstring>
#include <fstream>
#include <cstdlib>
#include <functional> 
#include <algorithm> 
#include <vector>
#include <map> 

#define lson l, mid, rt << 1
#define rson mid + 1, r, rt << 1 | 1
using namespace std;

int const MAX = 1e5 + 5;
int sum[MAX << 2], lazy[MAX << 2], look[MAX << 1];

void PushUp(int rt)
{
    sum[rt] = max(sum[rt << 1], sum[rt << 1 | 1]); 
}

void PushDown(int rt, int ln, int rn)
{
    if(lazy[rt] != -1)
    {
        // 注意这里的max是必要的，e.g. [[2,13,10],[10,17,25],[12,20,14]]
        sum[rt << 1] = max(lazy[rt], sum[rt << 1]); 
        sum[rt << 1 | 1] = max(lazy[rt], sum[rt << 1 | 1]); 
        lazy[rt << 1] = max(lazy[rt], lazy[rt << 1]); 
        lazy[rt << 1 | 1] = max(lazy[rt], lazy[rt << 1 | 1]); 
        lazy[rt] = -1;
    }
    return;
}

void Update(int L, int R, int val, int l, int r, int rt)
{
    if(L <= l && r <= R)
    {
        sum[rt] = max(lazy[rt], val);
        lazy[rt] = max(lazy[rt], val);
        return;
    }
    int mid = (l + r) >> 1;
    PushDown(rt, mid - l + 1, r - mid);
    if(L <= mid)
        Update(L, R, val, lson);
    if(mid < R)
        Update(L, R, val, rson);
    PushUp(rt);
    return;
}

int Query(int L, int R, int l, int r, int rt)
{
    if(L <= l && r <= R)
        return sum[rt];
    int mid = (l + r) >> 1;
    PushDown(rt, mid - l + 1, r - mid);
    int ans = 0;
    if(L <= mid)
        ans += Query(L, R, lson);
    if(mid < R)
        ans += Query(L, R, rson);
    return ans;
}


class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
    	int n = buildings.size();
    	memset(sum, 0, sizeof(sum));
    	memset(lazy, -1, sizeof(lazy));
    	int look_len = 0;
    	int leftmost = MAX; int rightmost = 0;
    	for(int i = 0; i < n; i++){
			int l, r, h;
			l = buildings[i][0];
			r = buildings[i][1];
			look[look_len++] = l;
			look[look_len++] = r;
		}
		sort(look, look + look_len);
		look_len = unique(look, look + look_len) - look;
//		for(int i = 0; i < look_len; i++){
//			printf("%d ", look[i]);
//		}
//		puts("");
        // printf("%d %d\n", leftmost, rightmost);
    	for(int i = 0; i < n; i++){
			int l, r, h;
			l = buildings[i][0];
			r = buildings[i][1];
			h = buildings[i][2];
			int ll = lower_bound(look, look + look_len, l) - look + 1;
			int rr = lower_bound(look, look + look_len, r) - look + 1;
            Update(ll, rr - 1, h, 1, look_len, 1);
		}
        vector<pair<int, int>> ans;
        int prev = 0;
    	for(int i = 0; i < look_len; i++){
            int cur = Query(i + 1, i + 1, 1, look_len, 1);
            if (cur != prev){
//            printf("%d %d\n", look[i], cur);
            	ans.push_back(make_pair(look[i], cur));
				prev = cur;
			}
		}
        return ans;
    }
};

int main()
{
	Solution sln;
	vector<vector<int>> v = { {2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8} };
	vector<pair<int, int>> ans = sln.getSkyline(v);
	v = {{1,2,1},{2147483646,2147483647,2147483647}};
	ans = sln.getSkyline(v);
	
}
