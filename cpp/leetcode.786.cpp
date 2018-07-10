#include <bits/stdc++.h>

using namespace std;

#define LL long long
#define pii pair<int, int>

vector<int> * pnums;
#define arr (*pnums)
int vis[2010][2010];
int n;

struct Node{
    int p;
    int q;
    Node(int a, int b): p(a), q(b){}
    bool operator<(const Node & other) const{
        return arr[this->p] * 1.0 / arr[this->q] > arr[other.p] * 1.0 / arr[other.q];
    }
};

bool valid(int p, int q){
    return(0 <= p && p < n and p < q && q < n) && !vis[p][q];
}

priority_queue<Node> pq;
class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& A, int K) {
        while(!pq.empty()){
            pq.pop();
        }
        memset(vis, 0, sizeof vis);
        pnums = &A;
        n = A.size();
        int k = K;
        pq.push(Node(0, n - 1));
        vis[0][n - 1] = 1;

        while(!pq.empty()){
            Node node = pq.top();
            pq.pop();
            int p = node.p;
            int q = node.q;
            k --;
            if (k == 0){
                return vector<int>{arr[p], arr[q]};
            }
            if (valid(p + 1, q)){
                vis[p + 1][q] = 1;
                pq.push(Node(p + 1, q));
            }
            if (valid(p, q - 1)){
                vis[p][q - 1] = 1;
                pq.push(Node(p, q - 1));
            }
        }
    }
};

//void print_list(const vector<int> & lst){
//    for(int x : lst){
//        printf("%d ", x);
//    }
//    puts("");
//}
//
//int main(){
//    Solution sln;
//    vector<int> vec = vector<int>{1, 2, 3, 5};
//    print_list(sln.kthSmallestPrimeFraction(vec, 3));
//
//    vec = vector<int>{1, 7};
//    print_list(sln.kthSmallestPrimeFraction(vec, 1));
//
//    vec = vector<int>{1,7,23,29,47};
//    print_list(sln.kthSmallestPrimeFraction(vec, 8));
//    return 0;
//}
