#include <iostream>
#include <vector>

using namespace std;

int N;
vector<long long> a;

int main() {
    cin >> N;
    a.resize(N);
    for (int i = 0; i < N; i++) cin >> a[i];
    long long ans = 0;
    for (int i = 0; i < N; i++) {
        int tmp = 0;
        while (a[i] % 2 == 0) {
            tmp++;
            a[i] /= 2;
        }
        ans += tmp;
    }
    cout << ans << endl;
}
