#include <iostream>
#include <string>

#define rep(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    string S;
    cin >> S;

    int res = 1 << 29;
    for (int start = 0; start <= 1; ++start) {
        int val = start;
        int cnt = 0;
        for (int i = 0; i < S.size(); ++i) {
            if (S[i] - '0' != val) cnt++;
            val = 1 - val;
        }
        res = min(res, cnt);
    }
    cout << res << endl;
    return 0;
}