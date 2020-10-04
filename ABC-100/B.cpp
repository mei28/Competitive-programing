#include <bits/stdc++.h>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int d, n;

int main() {
    cin >> d >> n;
    if (n == 100) n++;
    if (d == 0) {
        cout << n << endl;
    }
    if (d == 1) {
        cout << 100 * n << endl;
    }
    if (d == 2) {
        cout << 10000 * n << endl;
    }
}
