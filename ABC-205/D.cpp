#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n, q;
  cin >> n >> q;
  vector<long long> A(n);

  for (auto &x : A) {
    cin >> x;
  }
  vector<long long> low(n);
  for (int i = 0; i < n; ++i) {
    low[i] = A[i] - (i + 1);
  }

  while (q--) {
    long long k;
    cin >> k;
    const int idx = lower_bound(low.begin(), low.end(), k) - low.begin();
    if (idx == n) {
      cout << A[n - 1] + (k - low[n - 1]) << "\n";
    } else {
      cout << A[idx] - (low[idx] - k + 1) << '\n';
    }
  }
  return 0;
}
