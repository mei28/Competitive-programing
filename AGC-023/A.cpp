#include <iostream>
#include <map>
#include <vector>

using namespace std;
using Int = long long;

int main() {
  int n;
  cin >> n;
  vector<Int> A(n, 0);

  for (auto &e : A)
    cin >> e;
  vector<Int> S(n + 1, 0);

  for (int i = 0; i < n; ++i) {
    S[i + 1] = S[i] + A[i];
  }

  map<Int, Int> nums;
  for (int i = 0; i < n+1; ++i) {
    nums[S[i]]++;
  }

  Int ans = 0;
  for (auto it : nums) {
    Int num = it.second;
    ans += num * (num - 1) / 2;
  }
  cout << ans << endl;
  return 0;
}
