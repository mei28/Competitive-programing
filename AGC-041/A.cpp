#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
using ll = long long;

int main() {
    ll n, a, b;
    cin >> n >> a >> b;
    if ((b - a) % 2 == 0) {
        cout << (b - a) / 2 << endl;
    } else {
        cout << min(a + (b - a - 1) / 2, n - b + 1 + (b - a - 1) / 2) << endl;
    }
    return 0;
}