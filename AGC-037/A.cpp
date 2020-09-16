#include <bits/stdc++.h>
using namespace std;

template <class T>
bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return 1;
    }
    return 0;
}

// ====================================================================

int main() {
    string s;
    cin >> s;
    int dp[s.size() + 1][3];  // 読みやすいように3にしてる
    memset(dp, 0, sizeof(dp));

    // DPをする、dp[i][1,2]…i文字目までで、直近の文字の長さが1or2
    dp[1][0] = dp[2][1] = 1;
    for (int i = 0; i <= s.size(); i++) {
        if (i >= 1 && s[i - 1] != s[i])  // 1→1
            chmax(dp[i + 1][1], dp[i][1] + 1);
        if (i >= 2 && s[i - 2] != s[i] || s[i - 1] != s[i + 1])  // 2→2
            chmax(dp[i + 2][2], dp[i][2] + 1);
        chmax(dp[i + 2][2], dp[i][1] + 1);  // 1→2
        chmax(dp[i + 1][1], dp[i][2] + 1);  // 2→1
    }

    cout << max(dp[s.size()][1], dp[s.size()][2]) << endl;

}
