#include <iostream>

using namespace std;
using ll = long long;
int main() {
    ll a, b;
    cin >> a >> b;
    if (a < 0) {
        if (b >= 0)
            cout << "Zero" << endl;
        else if (abs(abs(b) -abs(a))% 2 != 0)
            cout << "Positive" << endl;
        else
            cout << "Negative" << endl;
    } else
        cout << "Positive" << endl;
    return 0;
}