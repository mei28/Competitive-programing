#include <iostream>
#include <vector>

using namespace std;

struct UnionFind {
  vector<int> par;

  UnionFind(int n) : par(n) {
    for (int i = 0; i < n; i++)
      par[i] = -1;
  }

  int root(int x) {
    if (par[x] < 0)
      return x;
    return par[x] = root(par[x]);
  }

  void merge(int x, int y) {
    int rx = root(x);
    int ry = root(y);

    if (rx == ry)
      return;
    if (rx > ry)
      swap(rx, ry);
    par[rx] += par[ry];
    par[ry] = rx;
  }

  bool same(int x, int y) {
    int rx = root(x);
    int ry = root(y);
    return rx == ry;
  }
};

int main() {
  int n, m;
  cin >> n >> m;
  
  vector<int> d(n,0);
  UnionFind uf(n);
  for(int i=0;i<m;i++){
    int a,b;
    cin>>a>>b;
    a--;
    b--;

    if(uf.same(a,b)){
      cout<<"No"<<endl;
      return 0;
    }

    uf.merge(a,b);
    d[a]++;
    d[b]++;
  }

  for(int i=0;i<n;i++){
    if(d[i]>2){
      cout<<"No"<<endl;
      return 0;
    }
  }

  cout<<"Yes"<<endl;
  return 0;
}
