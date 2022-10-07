#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
using Int = long long;

#define all(x) x.begin(), x.end()

int LIS(const vector<int> &A) {
  vector<int> dp;
  for (auto &&x : A) {
    int i = lower_bound(all(dp), x) - dp.begin();
    if (i >= int(dp.size())) {
      dp.emplace_back(x);
    } else {
      dp[i] = x;
    }
  }
  return dp.size();
}

int main() {
  int N;
  cin >> N;
  vector<pair<int, int>> AB(N);

  for (int i = 0; i < N; i++)
    cin >> AB[i].first;
  for (int i = 0; i < N; i++)
    cin >> AB[i].second;
  sort(all(AB));
  vector<int> B(N);
  for (int i = 0; i < N; i++)
    B[i] = AB[i].second;
  cout<<N+LIS(B)<<endl;
  return 0;
}
