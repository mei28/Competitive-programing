#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> G(N + 1, 0);
    int left = 1, right = N;
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        left = max(left, a);
        right = min(right, b);
    }
    cout << max(right - left + 1, 0) << endl;
    return 0;
}