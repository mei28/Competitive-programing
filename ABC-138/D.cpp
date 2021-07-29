#include <vector>
#include <iostream>

using namespace std;

using Graph = vector<vector<int>>;
int n,q;
Graph G;

void dfs(int v, int p, vector<long long> &res) {
  if (p != -1) res[v] += res[p];
  for (auto e : G[v]) {
    if (e == p) continue;
    dfs(e, v, res);
  }
}
int main(){
    cin>>n>>q;
    G.assign(n,vector<int>());

    for(int i=0;i<n-1;i++){
        int a=0,b=0;
        a--;
        b--;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    vector<long long> val(n,0);
    for(int i=0; i<q; i++){
        int p=0,x=0;
        p--;
        val[p] += x;
    }
    dfs(0,-1,val);
    for(auto v: val){
        cout<< v<< " ";
    }
    cout<<endl;
    return 0;
}
