#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<long long> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // ソート
    sort(a.begin(), a.end());

    // K 差の最小値
    long long res = 1LL << 60;  // INF の気持ち
    for (int i = 0; i + K - 1 < N; ++i) res = min(res, a[i + K - 1] - a[i]);
    cout << res << endl;
}