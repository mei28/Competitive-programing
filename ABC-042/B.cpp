#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n, l;
    cin >> n >> l;
    vector<string> S(n);
    for (int i = 0; i < n; ++i) cin >> S[i];
    sort(S.begin(), S.end());
    for (int i = 0; i < n; i++) {
        cout << S[i];
    }
    cout << endl;
    return 0;
}