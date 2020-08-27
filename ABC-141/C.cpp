#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K, Q;
    cin >> N >> K >> Q;
    vector<int> num(N, 0);

    for (int i = 0; i < Q; ++i) {
        int a;
        cin >> a;
        a--;
        num[a]++;
    }

    for (int i = 0; i < N; ++i) {
        if (K - (Q - num[i]) <= 0)
            cout << "No" << endl;
        else
            cout << "Yes" << endl;
    }
    return 0;
}