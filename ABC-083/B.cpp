#include <iostream>

using namespace std;

int main() {
    int n, a, b;
    cin >> n >> a >> b;
    int cnt = 0;
    for (int i = 1; i <= n; ++i) {
        int c = 0;
        int t = i;
        for (int j = 0; j < 5; j++) {
            c += t % 10;
            t /= 10;
        }
        if (a <= c && c <= b) cnt += +i;
    }
    cout << cnt << endl;
    return 0;
}