#include <iostream> 
#include <fstream>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <functional>
#include "stdlib.h" 
#include "time.h"
#include <set>
#include <map>
#include <numeric>
#include <cctype>
#include <cmath>
#include <sstream>

#define INF 0x3f3f3f3f
#define MOD 100000007
#define MAXN 510
using namespace std;
#define LL long long
#define ULL unsigned long long
#define LD long double
typedef pair<int, int> pii;


struct TreeNode {     
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

std::map<TreeNode *, TreeNode *> fa;

TreeNode * find(TreeNode * node) {
    if (fa.find(node) == fa.end()) {
        fa[node] = node;
    }
    while (fa[node] != node) {
        node = fa[node];
    }
    return node;
}

TreeNode * merge(TreeNode * a, TreeNode * b) {
    TreeNode * ffa = find(a);
    TreeNode * ffb = find(b);
    fa[ffb] = ffa;
    return ffa;
}

class Solution {
public:
    TreeNode* p = nullptr; 
    TreeNode* q = nullptr; 
    TreeNode* ans = nullptr;
    bool vp = false, vq = false;
    void dfs(TreeNode * cur) {
        if (cur->left)
        {
            dfs(cur->left);
            merge(cur, cur->left);
        }
        if (cur->right)
        {
            dfs(cur->right);
            merge(cur, cur->right);
        }
        if (cur == p)
        {
            vp = true;
            if (vq)
            {
                this->ans = find(q);
            }
        }
        if (cur == q)
        {
            vq = true;
            if (vq)
            {
                this->ans = find(p);
            }
        }
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        fa.clear();
        this->p = p;
        this->q = q;
        ans = nullptr;
        vp = false, vq = false;
        dfs(root);
        return this->ans;
    }
};

int main() {
    std::vector<TreeNode *> t = { new TreeNode(999), new TreeNode(2), new TreeNode(3) };
    t[0]->left = t[1];
    t[0]->right = t[2];
    Solution sln = Solution();
    TreeNode * ans = sln.lowestCommonAncestor(t[0], t[1], t[2]);
    printf("%d\n", ans->val);

    t = { new TreeNode(999), new TreeNode(2), new TreeNode(3) };
    t[0]->left = t[1];
    t[1]->right = t[2];
    ans = sln.lowestCommonAncestor(t[0], t[0], t[2]);
    printf("%d\n", ans->val);

    system("pause");
}
