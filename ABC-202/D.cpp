#include <iostream>
#include <string>

using namespace std;
using Int = long long;

Int perm(Int a, Int b) {
  Int res = 1;
  for (Int i = 1; i <= a; ++i) {
    res *= b + 1;
    res /= i;
  }
  return res;
}

int main() {
  int a, b;
  Int k;
  cin >> a >> b >> k;

  Int now = 0;
  string ans = "";

  while (a + b > 0) {
    if (a == 0) {
      ans += 'b';
      b--;
      continue;
    } else if (b == 0) {
      ans += 'a';
      a--;
      continue;
    }

    Int next = perm(a - 1, b);
    if (next + now < k) {
      b--;
      now += next;
      ans += 'b';
    } else {
      a--;
      ans += 'a';
    }
  }
  cout << ans << endl;
  return 0;
}
