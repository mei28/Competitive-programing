#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long> H(N);
    for (int i = 0; i < N; ++i) cin >> H[i];

    int cnt = 0;
    int tmp_cnt = 0;

    for (int i = 1; i < N; ++i) {
        if (H[i - 1] >= H[i]) {
            tmp_cnt++;
            cnt = max(tmp_cnt, cnt);
        } else
            tmp_cnt = 0;
    }
    cout << cnt << endl;
    return 0;
}