#include <iostream>
#include <string>
#include <vector>

using namespace std;

string S;
int k;
bool check(int ans) {
  for (int i = 0; i <= S.length() - ans; ++i) {
    int cnt_x = 0;
    for (int j = 0; j < ans; ++j) {
      if (S[i + j] == '.') {
        cnt_x++;
        if (cnt_x > k) {
          i += j ;
          break;
        }
      }
      if (j >= ans - 1)
        return true;
    }
  }
  return false;
}

int main() {
  cin >> S;
  cin >> k;
  int ok, ng;
  ok = 0;
  ng = S.length() + 1;

  while (ng - ok > 1) {

    int m = (ok + ng) / 2;
    if (check(m))
      ok = m;
    else
      ng = m;
  }

  cout << ok << endl;
  return 0;
}
