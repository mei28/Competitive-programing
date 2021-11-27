#include <iostream>
#include <vector>

using Int = long long;
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<Int> A(n);
  for (auto &e : A)
    cin >> e;
  sort(A.begin(), A.end());

  vector<Int> S(n + 1, 0);
  for (int i = 0; i < n; i++)
    S[i + 1] = S[i] + A[i];

  Int res = 0;
  for (int i = 0; i < n; ++i)
    res += A[i] * i - S[i];
  cout << res << endl;
  return 0;
}
