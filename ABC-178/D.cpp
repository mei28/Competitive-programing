#include <iostream>
#include <vector>

using namespace std;
using Int = long long;

const Int MOD = 1000000007;

int main() {
  int S;
  cin >> S;

  vector<Int> dp(S + 1, 0);
  dp[0] = 1;

  for (int i = 0; i <= S; i++) {
    for (int j = 0; j <= i - 3; j++) {
      dp[i] += dp[j];
      dp[i] %= MOD;
    }
  }

  cout << dp[S] << endl;
  return 0;
}
