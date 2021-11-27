#include <iostream>
#include <vector>

using Int = long long;
using namespace std;

int main() {
  string s;
  cin >> s;
  Int k;
  cin >> k;

  Int n = s.size();
  /* 累積和
    cnt[r]-cnt[l]によってs[l,r)の'.'の数がわかる
*/
  vector<Int> cnt(n + 1);
  for (int i = 0; i < n; ++i) {
    cnt[i + 1] = cnt[i];
    if (s[i] == '.')
      cnt[i + 1]++;
  }

  Int ans = 0;
  Int r = 0;

  for (Int l = 0; l < n; l++) {
    while (r <= n - 1 && cnt[r + 1] - cnt[l] <= k) {
      r++;
    }
    ans = max(ans,r-l);
  }
    cout<<ans<<endl;

  return 0;
}
