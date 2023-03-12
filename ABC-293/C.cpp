#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using Int = long long;
Int h = 0, w = 0;
bool check(const vector<Int> &l, const vector<vector<Int>> &A) {
  Int x = 0, y = 0;
  set<Int> ret;
  ret.insert(A[x][y]);
  for (Int i : l) {
    if (i == 1) {
      x += 1;
    }
    if (i == 0) {
      y += 1;
    }
    if (ret.count(A[x][y])) {
      return false;
    }
    ret.insert(A[x][y]);
  }
  return true;
}

int main() {
  cin >> h >> w;
  vector<vector<Int>> A(h, vector<Int>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> A[i][j];
    }
  }

  vector<Int> P(h + w - 2, 1);
  for (Int i = 0; i < h -1; i++) {
    P[i] = 0;
  }

  Int ans = 0;
  do {
    if (check(P, A)) {
      ans += 1;
    }
  } while (next_permutation(P.begin(), P.end()));
  cout << ans << endl;
  return 0;
}
