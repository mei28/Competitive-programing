#include <algorithm>
#include <iostream>
#include <vector>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<int> B(N - 1);
    rep(i, N - 1) cin >> B[i];

    ll res = B[0] + B.back();
    for (int i = 0; i + 1 < B.size(); i++) {
        res += min(B[i], B[i + 1]);
    }
    cout << res << endl;
    return 0;
}