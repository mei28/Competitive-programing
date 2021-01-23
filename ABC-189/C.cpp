#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<ll> A(N, 0);
    for (int i = 0; i < N; ++i) cin >> A[i];
    ll max_ = 0;
    for (int l = 0; l < N; ++l) {
        ll m = A[l];
        for (int r = l; r < N; r++) {
            m = min(A[r], m);
            max_ = max(max_, m * (r - l + 1));
        }
    }
    cout << max_ << endl;
    return 0;
}