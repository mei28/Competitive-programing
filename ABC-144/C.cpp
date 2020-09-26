#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;
    long long res = N + 1 - 2;  // (a, b) = (1, N)
    for (long long a = 1; a * a <= N; ++a) {
        if (N % a == 0) res = min(res, a + N / a - 2);
    }
    cout << res << endl;
}