#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    int T, A;
    cin >> T >> A;
    vector<int> H(N);
    for (int i = 0; i < N; i++) cin >> H[i];

    double min_diff = 999999;
    int min_idx = -1;
    for (int i = 0; i < N; ++i) {
        int h = H[i];
        double t = T - h * 0.006;
        if (min_diff > (abs(double(A) - double(t)))) {
            min_diff = abs(double(A) - double(t));
            min_idx = i;
        }
    }
    cout << min_idx + 1 << endl;
    return 0;
}