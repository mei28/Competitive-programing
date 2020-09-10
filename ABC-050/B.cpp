#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int n;
    cin >> n;
    vector<int> T(n);
    rep(i, n) cin >> T[i];
    ll sum = 0;
    rep(i, n) sum += T[i];
    int m;
    cin >> m;
    vector<int> P(m), X(m);
    rep(i, m) cin >> P[i] >> X[i];
    for (int i = 0; i < m; i++) {
        int idx = P[i] - 1;
        cout << sum - T[idx] + X[i] << endl;
    }
    return 0;
}