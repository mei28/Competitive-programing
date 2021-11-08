#include <iostream>
#include <vector>

using namespace std;
using Graph = vector<vector<int>>;

vector<bool> seen;

void dfs(const Graph &G, int v) {
  seen[v] = true;
  for (auto next_v : G[v]) {
    if (seen[next_v])
      continue;
    dfs(G, next_v);
  }
}

int main() {
  int n;
  cin >> n;
  Graph G(n);
  vector<int> T;

  for (int i = 0; i < n; i++) {
    int t, k;
    cin >> t >> k;
    T.push_back(t);
    for (int j = 0; j < k; j++) {
      int a;
      cin >> a;
      a--;
      G[i].push_back(a);
    }
  }

  seen.assign(n, false);
  dfs(G, n - 1);

  long long ans = 0;
  for (int i = 0; i < n; i++) {
    if (seen[i]) {
      ans += T[i];
    }
  }

  cout<<ans<<endl;

  return 0;
}
