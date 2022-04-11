#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> P(n,0);
  for (auto &e : P)
    cin >> e;
  priority_queue<int, vector<int>, greater<int>> pq;

  for (auto e : P)
    pq.push(e);

  cout << pq.top() << endl;
  for (int i = k; i < n; i++) {
    if (pq.top() < P[i]) {
      pq.pop();
      pq.push(P[i]);
    }
    cout << pq.top() << endl;
  }

  return 0;
}
