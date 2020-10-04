#include <bits/stdc++.h>

using namespace std;

int main() {
    long long q, h, s, d, n;
    cin >> q >> h >> s >> d >> n;
    long long one = min({q * 4, h * 2, s});
    cout << min(one * n, d * (n / 2) + one * (n % 2)) << endl;
    return 0;
}