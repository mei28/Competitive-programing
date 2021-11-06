#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> dp(65, vector<int>(2, 0));
int n;

int main() {
  cin >> n;

  // dp[i][j]: i=0 false, i=1 true j番目の時のこすう
  dp[0][0] = 1;
  dp[0][1] = 1;

  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    if (s == "AND") {
      dp[i + 1][0] = dp[i][0] * 2 + dp[i][1];
      dp[i + 1][1] = dp[i][1];
    } else {
      dp[i + 1][0] = dp[i][0];
      dp[i + 1][1] = dp[i][0] + dp[i][1] * 2;
    }
  }

  cout << dp[n][1] << endl;
  return 0;
}
