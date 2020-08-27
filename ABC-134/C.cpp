#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N), B(N);

    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        B[i] = A[i];
    }
    sort(B.begin(), B.end());
    reverse(B.begin(), B.end());
    int fst = B[0], sec = B[1];
    for (int i = 0; i < N; ++i) {
        if (A[i] == fst)
            cout << sec << endl;
        else
            cout << fst << endl;
    }
    return 0;
}