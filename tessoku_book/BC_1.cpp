#include <iostream>
#include <set>
using namespace std;

int main() {
  int q;
  cin >> q;
  set<int> S;
  while (q--) {
    int a, x;
    cin >> a >> x;
    if (a == 1) {
      S.insert(x);
    }
    if (a == 2) {
      S.erase(x);
    }
    if (a == 3) {
      auto it = S.lower_bound(x);
      if (it == S.end()) {
        cout << -1 << endl;
      } else {
        cout << *it << endl;
      }
    }
  }

  return 0;
}
