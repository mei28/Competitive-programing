#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool my_compare(pair<string, int> a, pair<string, int> b) {
    if (a.second == b.second) {
        return a.first.compare(b.first) < 0;
    }
    return a.second > b.second;
}

int main() {
    int N;
    cin >> N;
    map<string, int> m;
    string S;
    for (int i = 0; i < N; i++) {
        cin >> S;
        if (m.count(S)) {
            m[S]++;
        } else {
            m[S] = 1;
        }
    }
    vector<pair<string, int>> v;
    for (auto it = m.begin(); it != m.end(); it++) {
        v.push_back(make_pair(it->first, it->second));
    }
    sort(v.begin(), v.end(), my_compare);
    int t = v[0].second;
    for (int i = 0; i < v.size(); i++) {
        if (v[i].second == t) {
            cout << v[i].first << "\n";
        }
    }
    return 0;
}