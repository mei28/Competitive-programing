#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int x;
    cin >> x;
    int ans = 1;
    for (int i = 1; i <= x; i++) {
        for (int j = 2; j <= x; j++) {
            int tmp = pow(i, j);
            if (tmp <= x) {
                ans = max(tmp, ans);
            } else
                break;
        }
    }
    cout << ans << endl;
    return 0;
}