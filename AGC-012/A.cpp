#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N * 3);
    for (int i = 0; i < N * 3; ++i) cin >> A[i];
    sort(A.begin(), A.end(), greater<long long>());
    long long res = 0;
    for (int i = 1, j = 0; j < N; i += 2, ++j) res += A[i];
    cout << res << endl;
}