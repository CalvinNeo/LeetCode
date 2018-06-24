#include <bits/stdc++.h>


#define LL long long
using namespace std;

int nums[100];
int ans = -1;
int n, k;
int ppos;

LL get_count(LL node){
    // 以node为前缀的不超过n的数量
    LL gap = 0;
    LL p = node;
    LL q = node + 1;
    while(p <= n){
        gap += max(0ll, min((LL)(n + 1), q) - p);
        p *= 10;
        q *= 10;
    }
    return gap;
}

class Solution {
public:
    int findKthNumber(int nn, int kk) {
        n = nn;
        k = kk;
        memset(nums, 0, sizeof nums);
        ans = -1;
        ppos = 0;
        int x = n;
        while (x != 0) {
            nums[ppos++] = x % 10;
            x /= 10;
        }
        int counter = k;

        LL prefix = 1;
//        counter --;
        while(counter > 0){
            LL node_cnt = get_count(prefix);
//            printf("count %d = %d\n", prefix, node_cnt);
            if(counter > node_cnt){
                counter -= node_cnt;
//                printf("AAAAA %d\n", counter);
                prefix ++;
            }
            else if(counter == node_cnt){
                counter --;
//                printf("BBBBB %d\n", counter);
                if(counter != 0){
                    prefix *= 10;
                }
            }
            else{
                counter --;
//                printf("CCCCC %d\n", counter);
                if(counter != 0){
                    prefix *= 10;
                }
            }
        }
        return (int)prefix;
    }
};