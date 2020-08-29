#include <iostream>

using namespace std;
using ll = long long;

int main() {
    ll A, B, C, K;
    cin >> A >> B >> C >> K;
    ll diff = A - B;
    if (abs(diff) >= 1e18) {
        cout << "Unfair" << endl;
        return 0;
    }
    if (K % 2 == 0) {
        cout << diff << endl;
    } else {
        cout << -diff << endl;
    }
    return 0;
}