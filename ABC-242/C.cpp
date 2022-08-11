#include <iostream>
#include <string>

using namespace std;
int cnt, n;
int MOD = 998244353;

void dfs(string A) {

  if (A.length() == n) {
    cnt++;
    cnt %= MOD;
    return;
  }

  for (int di = -1; di < 2; di++) {
    int _n = A.length();
    if (A[_n - 1] == '1' && di == -1) {
      continue;
    }
    if (A[_n - 1] == '9' && di == 1) {
      continue;
    }

    A += to_string(int(A[_n - 1] - '0') + di);
    cout<<A<<endl;
    dfs(A);
    A = A.substr(0, _n - 1);
  }
}

int main() {
  cin >> n;
  for (int i = 1; i < 10; i++) {
    dfs(to_string(i));
  }
  cout << cnt << endl;
  return 0;
}
