#include <iostream>

using namespace std;
using Int = long long;
int main(void) {
  Int n, ans, k;
  cin >> n;
  for (Int i = 1; i <= n; i++) {
    if (i * i <= n)
      k = i;
    else
      break;
  }
  ans = 0;
  for (Int i = 1; i <= k; i++)
    ans += ((n / i) - (n / (i + 1))) * i;
  for (Int i = 1; i <= n / (k + 1); i++)
    ans += (n / i);

  cout << ans << endl;
  return 0;
}
