#include <iostream>
#include <vector>

using namespace std;
using Int = long long;
const Int MOD = 1000000007;

vector<int> dp_plus(110000);
vector<int> dp_minus(110000);

int main() {
  dp_plus[0] = 1;
  dp_plus[1] = dp_minus[1] = 1;

  for (int i = 2; i < 110000; i++) {
    dp_plus[i] = dp_plus[i - 1] + dp_minus[i - 1];
    dp_plus[i] %= MOD;
    dp_minus[i] = dp_plus[i - 1];
    dp_minus[i] %= MOD;
  }

  int n;
  cin >> n;
  vector<int> a(n);
  for (auto &e : a)
    cin >> e;
  Int ans = 0;

  ans += a[0] * (dp_plus[n - 1] + dp_minus[n - 1]);
  if (n > 1)
    ans += a[n - 1] * (dp_minus[n - 2]);

  for (int i = 1; i < n - 1; i++) {
    int l = i - 1;
    int r = n - i - 1;
    ans += a[i] * (dp_plus[l] + dp_minus[l]) % MOD *
           (dp_plus[r] + dp_minus[r]) % MOD;
    ans %= MOD;
    ans -= a[i] * dp_plus[l] % MOD * dp_plus[r] % MOD;
  }

  cout << ans << endl;

  return 0;
}
