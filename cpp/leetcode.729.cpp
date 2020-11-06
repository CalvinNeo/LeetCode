#include<bits/stdc++.h>

#define LL long long

#define lson l, mid, root << 1
#define rson mid + 1, r, root << 1 | 1
#define inf 0x3f3f3f3f
using namespace std;

int const MAX = 1e9 * 2;

struct Node {
    // Whether there exists 1 in this range
    int data = 0;

    Node * left = nullptr;
    Node * right = nullptr;

    ~Node(){
        delete left;
        delete right;
    }
};

void update(Node * root, int fr, int to, int l, int r, int val){
    if(fr <= l && r <= to)
    {
//        printf("Set range [%d,%d] to 1\n", l, r);
        root->data = 1;
        return;
    }
    int mid = (l + r) >> 1;
    if(fr <= mid){
        if(!root->left){
            root->left = new Node();
        }
        update(root->left, fr, to, l, mid, val);
    }
    if(mid < to){
        if(!root->right){
            root->right = new Node();
        }
        update(root->right, fr, to, mid + 1, r, val);
    }
    int ll = 0, rr = 0;
    if(root->left){
        ll = root->left->data;
    }
    if(root->right){
        rr = root->right->data;
    }
    root->data = ll | rr;
}

int query(Node * root, int fr, int to, int l, int r){
    if(r < fr || l > to){
        return 0;
    }
    int mid = (l + r) >> 1;
    int ans = 0;
    if(fr <= l && r <= to){
//        printf("in [%d,%d] find [%d,%d] root=%d ans=%d mid=%d\n", l, r, fr, to, root->data, root->data, mid);
        return root->data;
    }
    if(!root->left && !root->right){
        // IMPORTANT
        ans = root->data;
    }else{
        if(root->left){
            ans |= query(root->left, fr, to, l, mid);
        }else{
    //        printf("No left [%d,%d]\n", l, mid);
        }
        if(root->right){
            ans |= query(root->right, fr, to, mid + 1, r);
        }else{
    //        printf("No right [%d,%d]\n", mid + 1, r);
        }
    }
//    printf("in [%d,%d] find [%d,%d] root=%d ans=%d mid=%d\n", l, r, fr, to, root->data, ans, mid);
    return ans;
}

void print_list(const vector<int> & l){
    for(int i = 0; i < l.size(); i ++){
        printf("%d ", l[i]);
    }
    puts("");
}

class MyCalendar {
public:
    Node * root;
    MyCalendar() {
        root = new Node();
    }
    bool book(int s, int e) {
        bool ans = !query(root, s, e - 1, 0, MAX);
//        printf("check %d\n", ans);
        if(ans){
            update(root, s, e - 1, 0, MAX, 1);
//            puts("===========4");
        }
        return ans;
    }
    ~MyCalendar() {
        delete root;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * int param_1 = obj.book(start,end);
 */

//int main(){
//    MyCalendar mc;
//    printf("%d\n", mc.book(10, 20)); // returns 1
//    printf("%d\n", mc.book(15, 25)); // returns 0
//    printf("%d\n", mc.book(20, 30)); // returns 1
////
////    vector<vector<int>> vec = {{69,70},{3,4},{39,40},{35,36},{3,4},{55,56},{61,62},{97,98},{79,80},{76,77},{46,47},{78,79},{47,48},{38,39},{83,84},{90,91},{90,91},{49,50},{49,50},{77,78},{23,24},{89,90},{8,9},{3,4},{2,3},{48,49},{96,97},{4,5},{54,55},{30,31},{97,98},{65,66},{93,94},{49,50},{24,25},{17,18},{53,54},{45,46},{53,54},{32,33},{37,38},{5,6},{50,51},{48,49},{14,15},{91,92},{79,80},{73,74},{28,29},{31,32},{98,99},{37,38},{19,20},{49,50},{54,55},{37,38},{98,99},{12,13},{24,25},{46,47},{74,75},{87,88},{64,65},{61,62},{68,69},{28,29},{43,44},{89,90},{64,65},{72,73},{69,70},{88,89},{68,69},{28,29},{20,21},{64,65},{17,18},{40,41},{88,89},{22,23},{8,9},{33,34},{13,14},{19,20},{53,54},{99,100},{24,25},{82,83},{77,78},{90,91},{72,73},{33,34},{73,74},{0,1},{25,26},{69,70},{73,74},{12,13},{33,34},{47,48},{26,27},{77,78},{95,96},{28,29},{77,78},{28,29},{87,88},{16,17},{42,43},{51,52},{44,45},{63,64},{24,25},{18,19},{0,1},{45,46},{65,66},{21,22},{37,38},{77,78},{97,98},{24,25},{83,84},{20,21},{29,30},{66,67},{29,30},{37,38},{63,64},{15,16},{85,86},{61,62},{0,1},{23,24},{96,97},{91,92},{90,91},{80,81},{18,19},{69,70},{3,4},{59,60},{21,22},{75,76},{54,55},{65,66},{34,35},{19,20},{79,80},{6,7},{24,25},{29,30},{35,36},{9,10},{0,1},{73,74},{65,66},{78,79},{32,33},{58,59},{25,26},{3,4},{78,79},{92,93},{37,38},{91,92},{5,6},{79,80},{94,95},{78,79},{38,39},{16,17},{81,82},{34,35},{16,17},{33,34},{42,43},{34,35},{89,90},{88,89},{33,34},{68,69},{92,93},{73,74},{64,65},{91,92},{44,45},{13,14},{97,98},{64,65},{31,32},{91,92},{1,2},{57,58},{21,22},{38,39},{70,71},{84,85},{50,51},{58,59}};
////    vector<vector<int>> vec = {{6,14},{0,7}};
////
////    for(auto iter = vec.begin(); iter != vec.end(); iter++){
////        printf("%d %d %d\n", (*iter)[0], (*iter)[1], mc.book((*iter)[0], (*iter)[1]));
////    }
//}
