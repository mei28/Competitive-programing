#include <iostream>
#include <vector>

#define rep(i,n) for (int i=0; i<(n);++i)
using namespace std;

int n;
vector<int> color;
// どの頂点に行けるか
vector<vector<int>> to;
// 何回か
vector<int> cnt;
vector<int> ans;


// p -> おや, 親にdfsしないような仕組み
void dfs(int v, int p=-1){
    if (cnt[color[v]]==0){
        ans.push_back(v+1);
    }
    cnt[color[v]]++;
    for(int u : to[v]){
        if(u==p)continue;
        dfs(u,v);
    }
    cnt[color[v]]--;
}
int main(){
    cin>>n;
    color = vector<int>(n);
    cnt = vector<int>(100005);
    rep(i,n) cin >> color[i];
    to.resize(n);

    rep(i,n-1){
        int a,b;
        cin >> a >> b ;
        --a;
        --b;
        to[a].push_back(b);
        to[b].push_back(a);
    }
    dfs(0);
    sort(ans.begin(),ans.end());
    for(int v: ans){
        cout<< v << endl;
    }
    return 0;
}
