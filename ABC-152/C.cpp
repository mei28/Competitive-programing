#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    int mi = N + 1, res = 0;
    for (int i = 0; i < N; ++i) {
        int p;
        cin >> p;
        mi = min(mi, p);
        if (mi == p) ++res;
    }
    cout << res << endl;
}