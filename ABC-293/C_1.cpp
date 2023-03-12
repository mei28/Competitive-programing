#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
  int h, w;
  cin >> h >> w;

  vector<vector<int>> A(h, vector<int>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> A[i][j];
    }
  }

  vector<char> P(h - 1, 'd');
  P.insert(P.end(), w - 1, 'r');

  int ans = 0;
  set<vector<int>> L;
  do {
    bool valid = true;
    set<int> ret;
    ret.insert(A[0][0]);
    int x = 0, y = 0;
    for (int i = 0; i < h + w - 2; i++) {
      if (P[i] == 'd') {
        y++;
      } else {
        x++;
      }
      if (ret.count(A[x][y])) {
        valid = false;
        break;
      }
      ret.insert(A[x][y]);
    }
    if (valid) {
      ans++;
    }
  } while (next_permutation(P.begin(), P.end()));

  cout << ans << endl;

  return 0;
}

