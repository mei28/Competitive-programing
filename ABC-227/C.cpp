#include <iostream>

using namespace std;

int main() {
  long long n;
  cin >> n;
  long long ans = 0;
  for (long long i = 0; i <= n; i++) {
    for (long long j = i; j <= n; j++) {
      long long k = n / i;
      k /= j;
      ans += k - j + 1;
    }
  }
  cout << ans << endl;
  return 0;
}
