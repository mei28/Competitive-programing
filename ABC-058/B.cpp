#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    string O, E;
    cin >> O >> E;
    if (O.size() == E.size()) {
        for (int i = 0; i < O.size(); ++i) {
            cout << O[i]  << E[i];
        }
        cout << endl;
    } else {
        for (int i = 0; i < O.size()-1; ++i) {
            cout << O[i] << E[i];
        }
        cout << O[O.size() - 1] << endl;
    }
    return 0;
}