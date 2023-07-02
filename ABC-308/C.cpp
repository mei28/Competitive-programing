#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<pair<ll, ll>, int> P;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<P> rates(N);
    for(int i = 0; i < N; i++) {
        ll Ai, Bi;
        cin >> Ai >> Bi;
        rates[i] = make_pair(make_pair(Ai, Ai + Bi), i);
    }

    sort(rates.begin(), rates.end(), [](const P& a, const P& b) {
        ll x1 = a.first.first * b.first.second;
        ll x2 = b.first.first * a.first.second;
        if (x1 != x2) {
            return x1 > x2;
        } else {
            return a.second < b.second;
        }
    });

    for(int i = 0; i < N; i++) {
        cout << rates[i].second + 1 << " ";
    }

    return 0;
}

