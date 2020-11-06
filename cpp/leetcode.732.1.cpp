#include<bits/stdc++.h>

#define LL long long

#define lson l, mid, root << 1
#define rson mid + 1, r, root << 1 | 1
#define inf 0x3f3f3f3f
using namespace std;

int const MAX = 10010;
int tree[MAX << 2], lazy[MAX << 2];

void PushUp(int root)
{
    tree[root] = max(tree[root << 1], tree[root << 1 | 1]);
}

void PushDown(int root, int ln, int rn)
{
    if(lazy[root] != -1)
    {
        tree[root << 1] = lazy[root] + tree[root << 1];
        tree[root << 1 | 1] = lazy[root] + tree[root << 1 | 1];
        lazy[root << 1] = lazy[root << 1] == -1 ? lazy[root] : lazy[root] + lazy[root << 1];
        lazy[root << 1 | 1] = lazy[root << 1 | 1] == -1 ? lazy[root] : lazy[root] + lazy[root << 1 | 1];
        lazy[root] = -1;
    }
    return;
}

void Update(int fr, int to, int val, int l, int r, int root)
{
    if(fr <= l && r <= to)
    {
        tree[root] += val;
        lazy[root] = val;
        return;
    }
    int mid = (l + r) >> 1;
    PushDown(root, mid - l + 1, r - mid);
    if(fr <= mid){
        Update(fr, to, val, lson);
    }
    if(mid < to){
        Update(fr, to, val, rson);
    }
    PushUp(root);
    return;
}

int Query(int fr, int to, int l, int r, int root)
{
    if(fr <= l && r <= to){
        return tree[root];
    }
    int mid = (l + r) >> 1;
    PushDown(root, mid - l + 1, r - mid);
    int ans = 0;
    if(fr <= mid){
        ans = max(ans, Query(fr, to, lson));
    }
    if(mid < to){
        ans = max(ans, Query(fr, to, rson));
    }
    return ans;
}

void Build(int l, int r, int root, int val){
    if(l == r){
        tree[root] = val;
        lazy[root] = val;
    }else if(l < r){
        int mid = (l + r) >> 1;
        Build(lson, val);
        Build(rson, val);
    }
}

void print_list(const vector<int> & l){
    for(int i = 0; i < l.size(); i ++){
        printf("%d ", l[i]);
    }
    puts("");
}

class MyCalendarThree {
public:
    MyCalendarThree() {
        memset(lazy, -1, sizeof(lazy));
        memset(tree, 0, sizeof(tree));
    }

    int book(int s, int e) {
        Update(s, e - 1, 1, 1, MAX, 1);
        return Query(s, e, 1, MAX, 1);
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */

int main(){
    MyCalendarThree mc;
    printf("%d\n", mc.book(10, 20)); // returns 1
    printf("%d\n", mc.book(50, 60)); // returns 1
    printf("%d\n", mc.book(10, 40)); // returns 2
    printf("%d\n", mc.book(5, 15)); // returns 3
    printf("%d\n", mc.book(5, 10)); // returns 3
    printf("%d\n", mc.book(25, 55)); // returns 3
}
