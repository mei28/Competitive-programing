#include <iostream>
using namespace std;
using Int = long long;

int main() {
  int N;
  cin >> N;
  int x[N], y[N], h[N];
  for (int i = 0; i < N; i++) {
    cin >> x[i] >> y[i] >> h[i];
  }

  for (int cx = 0; cx <= 100; cx++) {
    for (int cy = 0; cy <= 100; cy++) {
      int H = 0;
      for (int i = 0; i < N; i++) {
        if (h[i] == 0)
          continue;
        Int t = abs(x[i] - cx) + abs(y[i] - cy);
        if (H == 0) {
          H = t + h[i];
        } else if (H != t + h[i]) {
          H = 0;
          break;
        }
      }
      if (H == 0)
        continue;
      bool flg = true;
      for (int i = 0; i < N; i++) {
        if (h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0)) {
          flg = false;
          break;
        }
      }
      if (flg) {
        cout << cx << " " << cy << " " << H << endl;
        return 0;
      }
    }
  }
  return 0;
}
