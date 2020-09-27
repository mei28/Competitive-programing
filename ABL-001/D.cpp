#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> A(n);
    rep(i, n) cin >> A[i];
    vector<int> B;
    int idx = 0;
    B.push_back(A[idx]);
    idx++;
    for (int i = 1; i < n; ++i) {
        int a = A[i];
        int b = B[idx - 1];
        if (abs(a - b) <= k) {
            B.push_back(a);
            idx++;
        }
    }
    cout << B.size() << endl;
    return 0;
}