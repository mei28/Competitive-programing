#include <iostream>

using namespace std;
using Int = long long;

int fac[20];

int main() {
  fac[0] = 1;
  for (int i = 1; i < 12; i++) {
    fac[i] = fac[i - 1] * i;
  }
  int p = 0;
  int ans = 0;
  cin>>p;

  for (int i = 10; i > 0; i--) {
    while (p >= fac[i]) {
      ans++;
      p -= fac[i];
    }
  }
  cout << ans << endl;
  return 0;
}
