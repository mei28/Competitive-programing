#include <iostream>
#include <vector>

using namespace std;
using Int = long long;
using P = pair<Int, Int>;
int main() {
  Int N, D, L, R;
  vector<P> LR;
  cin >> N >> D;
  for (int i = 0; i < N; ++i) {
    cin >> L >> R;
    LR.emplace_back(L, R);
  }
  sort(begin(LR), end(LR), [](P &a, P &b) { return a.second < b.second; });

  Int ans = 0, x = -(1LL << 50);

  for (auto &[l, r] : LR) {
    if (x + D - 1 < l)
      ans++, x = r;
  }
  cout << ans << endl;

  return 0;
}
