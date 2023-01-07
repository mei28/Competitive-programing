#include <iostream>
#include <vector>
using namespace std;
using Int = long long
struct edge {
  int to;
  int cost;
};

typedef pair<int, int> P; // first: 最短距離, second: 頂点番号
Int MAX_V = 200001;
Int INF = 1000000;

Int V, d[MAX_V], cnt[MAX_V];
vector<edge> G[MAX_V]; // 隣接リスト表現

void dijkstra(int s) {
  fill(d, d + V, INF);
  d[s] = 0; // 始点sへの最短距離は0
  fill(cnt, cnt + V, 0);
  cnt[s] = 1; // 始点sへの最短経路数は1

  priority_queue<P, vector<P>, greater<P>>
      que; // 距離が小さい順に取り出せるようgreater<P>を指定
  que.push(P(0, s));
  while (!que.empty()) {
    P p = que.top();
    que.pop();
    int v = p.second; // 更新した頂点の中で距離が最小の頂点v
    if (d[v] < p.first) {
      continue;
    }
    for (auto e : G[v]) { // 頂点vから出る辺eを走査
      if (d[e.to] > d[v] + e.cost) {
        d[e.to] = d[v] + e.cost;
        que.push(P(d[e.to], e.to));
        cnt[e.to] =
            cnt[v]; // コストが更新された場合は直前の頂点への最短経路数で上書き
      } else if (d[e.to] == d[v] + e.cost) {
        cnt[e.to] +=
            cnt[v]; // コストが一致する場合はこれまでの最短経路数を足し合わせ
      }
    }
  }
}

int main(){
  int n,m;
  cin>>n>>m;

  return 0;
}
