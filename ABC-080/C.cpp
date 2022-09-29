#include <iostream>

#define rep(i, a, b) for (int i = a; i < b; i++)
using namespace std;
#define INF INT_MAX / 2
int N, F[101][11], P[101][11];
int main() {
  cin >> N;
  rep(i, 0, N) rep(j, 0, 10) cin >> F[i][j];
  rep(i, 0, N) rep(j, 0, 11) cin >> P[i][j];

  int ans = -INF;
  rep(bits, 1, 1 << 10) {
    int sm = 0;
    rep(i, 0, N) {
      int c = 0;
      rep(j, 0, 10) if ((bits>>j) & 1) if (F[i][j]) c++;
      sm += P[i][c];
    }
    ans = max(ans, sm);
  }
  cout << ans << endl;
  return 0;
}
