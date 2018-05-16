#include <queue>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

vector<int> mat[10000];
int vis[10000];

int sgn(int x){
    if(x == 0) return 0;
    if (x > 0) return 1;
    return -1;
}

class Solution {
public:
    bool cmp_word(const string & a, const string & b){
        if (a.size() != b.size()) return false;
        int hit = 0;
        for(int i = 0; i < a.size(); i++){
            if(a[i] != b[i]) hit ++;
        }
        return (hit == 1);
    }
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), beginWord) == wordList.end()){
            wordList.push_back(beginWord);
        }
        int beg, e;

        beg = find(wordList.begin(), wordList.end(), beginWord) - wordList.begin();
        auto ee = find(wordList.begin(), wordList.end(), endWord);
        if (ee == wordList.end()){
            return 0;
        }
        e = ee - wordList.begin();
        int n = wordList.size();

        for(int i = 0; i < n; i++)
            mat[i].clear();

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(cmp_word(wordList[i], wordList[j])){
                    mat[i].push_back(j);
                    // mat[j].push_back(i);
                }

        memset(vis, 0, sizeof vis);

        queue<pair<int, int>> q1;
        queue<pair<int, int>> q2;
        q1.push(make_pair(beg, 1));
        q2.push(make_pair(e, -1));
        vis[beg] = 1;
        vis[e] = -1;

        auto bfs = [&](queue<pair<int, int>> & q, int flag){
            int c, d;
            tie(c, d) = q.front();
            q.pop();
            for(int i = 0; i < mat[c].size(); i++){
                if(sgn(vis[mat[c][i]]) != flag){
                    // printf( "%s %d: %s -> %s\n", flag > 0 ? "q1" : "q2", d, wordList[c].c_str(), wordList[mat[c][i]].c_str());
                    if (sgn(vis[mat[c][i]]) == -flag){
                        return make_pair(true, abs(d - vis[mat[c][i]]));
                    }else{
                        vis[mat[c][i]] = d + flag;
                        q.push(make_pair(mat[c][i], d + flag));
                    }
                }
            }
            return make_pair(false, 0);
        };

        while ((! q1.empty()) || (! q2.empty())){
            if (! q1.empty()){
                bool ans; int dd;
                tie(ans, dd) = bfs(q1, 1);
                if (ans)
                    return dd;
            }
            if (! q2.empty()){
                bool ans; int dd;
                tie(ans, dd) = bfs(q2, -1);
                if (ans)
                    return dd;
            }
        }
        return 0;
    }
};
