#include<bits/stdc++.h>

#define LL long long

#define lson l, mid, root << 1
#define rson mid + 1, r, root << 1 | 1
using namespace std;

int const MAX = 10010;
int sum[MAX << 2], lazy[MAX << 2], look[MAX << 1], look_len;

void PushUp(int root)
{
    sum[root] = max(sum[root << 1], sum[root << 1 | 1]);
}

void PushDown(int root, int ln, int rn)
{
    if(lazy[root] != -1)
    {
        sum[root << 1] = max(lazy[root], sum[root << 1]);
        sum[root << 1 | 1] = max(lazy[root], sum[root << 1 | 1]);
        lazy[root << 1] = max(lazy[root], lazy[root << 1]);
        lazy[root << 1 | 1] = max(lazy[root], lazy[root << 1 | 1]);
        lazy[root] = -1;
    }
    return;
}

void Update(int fr, int to, int val, int l, int r, int root)
{
    if(fr <= l && r <= to)
    {
        sum[root] = max(lazy[root], val);
        lazy[root] = max(lazy[root], val);
        return;
    }
    int mid = (l + r) >> 1;
    PushDown(root, mid - l + 1, r - mid);
    if(fr <= mid)
        Update(fr, to, val, lson);
    if(mid < to)
        Update(fr, to, val, rson);
    PushUp(root);
    return;
}

int Query(int fr, int to, int l, int r, int root)
{
    if(fr <= l && r <= to)
        return sum[root];
    int mid = (l + r) >> 1;
    PushDown(root, mid - l + 1, r - mid);
    int ans = 0;
    if(fr <= mid)
        ans = max(ans, Query(fr, to, lson));
    if(mid < to)
        ans = max(ans, Query(fr, to, rson));
    return ans;
}

void print_list(const vector<int> & l){
    for(int i = 0; i < l.size(); i ++){
        printf("%d ", l[i]);
    }
    puts("");
}

class Solution {
public:
    vector<int> fallingSquares(vector<pair<int, int>>& positions) {
        vector<int> ans;
        memset(look, 0, sizeof look);
    	memset(lazy, -1, sizeof(lazy));
    	memset(sum, 0, sizeof(sum));
        for (int i = 0; i < positions.size(); i++){
            look[look_len++] = positions[i].first;
            look[look_len++] = positions[i].first - 1;
            look[look_len++] = positions[i].first + 1;
            look[look_len++] = positions[i].first + positions[i].second;
            look[look_len++] = positions[i].first + positions[i].second - 1;
            look[look_len++] = positions[i].first + positions[i].second + 1;
        }
		sort(look, look + look_len);
//        for(int i = 0; i < look_len; i ++){
//            printf("%d ", look[i]);
//        }
//        puts("");
		look_len = unique(look, look + look_len) - look;
		int tot = 0;
        for (int i = 0; i < positions.size(); i++){
            int l = lower_bound(look, look + look_len, positions[i].first) - look;
            int r = lower_bound(look, look + look_len, positions[i].first + positions[i].second) - look;
            int cur_height;

            if (l + 1 >= r){
                cur_height = min(Query(l + 1, l + 1, 1, look_len, 1), Query(r + 1, r + 1, 1, look_len, 1));
            }else{
                int lb = lower_bound(look, look + look_len, positions[i].first + 1) - look;
                int rb = lower_bound(look, look + look_len, positions[i].first + positions[i].second - 1) - look;
                cur_height = Query(lb + 1, rb + 1, 1, look_len, 1);
            }
            int new_height = cur_height + positions[i].second;
            Update(l + 1, r + 1, new_height, 1, look_len, 1);
            tot = max(tot, new_height);
//            printf("sum %d new %d tot %d\n", cur_height, new_height, tot);
            ans.push_back(tot);
        }
        return ans;
    }
};

//int main(){
//    Solution sln;
//    vector<pair<int, int>> in;
//    in = {{1,2}, {2,3}, {6,1}};
//    print_list(sln.fallingSquares(in)); // 2 5 5
//    in = {{100,100}, {200,100}};
//    print_list(sln.fallingSquares(in)); // 100 100
//    in = {{1,5}, {2,2}, {7,5}};
//    print_list(sln.fallingSquares(in)); // 5 7 7
//    in = {{9,7}, {1,9}, {3,1}};
//    print_list(sln.fallingSquares(in)); // 7 16 17
//}
