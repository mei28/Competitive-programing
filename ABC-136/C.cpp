#include <iostream>
#include <vector>

using namespace std;
using ll = long long;

int main() {
    int N;
    cin >> N;
    vector<int> H(N);
    for (int i = 0; i < N; i++) cin >> H[i];
    for (int i = 1; i < N; i++) {
        if (H[i - 1] > H[i]) {
            cout << "No" << endl;
            return 0;
            break;
        } else {
            if (H[i] != H[i - 1]) {
                H[i]--;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}