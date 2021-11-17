#include <iostream>
#include <vector>

template <class T> inline bool chmin(T &a, T b) {
  if (a > b) {
    a = b;
    return true;
  } else
    return false;
}

using namespace std;
using Int = long long;

int main() {
  int n;
  cin >> n;
  vector<vector<Int>> C(n, vector<Int>(n));
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; ++j)
      cin >> C[i][j];

  vector<Int> X(n), Y(n);

  auto solve = [&]() -> bool {
    Int minX = C[0][0], minY = C[0][0];
    for (int i = 0; i < n; ++i) {
      chmin(minX, C[i][0]);
      chmin(minY, C[0][i]);
    }
    for (int i = 0; i < n; ++i) {
      X[i] = C[i][0] - minX;
      Y[i] = C[0][i] - minY;
    }

    Int diff = C[0][0] - X[0] - Y[0];
    for (int i = 0; i < n; ++i)
      X[i] += diff;

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (X[i] + Y[j] != C[i][j])
          return false;
      }
    }
    return true;
  };

  if (solve()) {
    cout << "Yes" << endl;
    for (auto e : X)
      cout << e << " ";
    cout << endl;
    for (auto e : Y)
      cout << e << " ";
    cout << endl;
  } else
    cout << "No" << endl;

  return 0;
}
