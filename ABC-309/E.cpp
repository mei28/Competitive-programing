#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<int> p(N+1);
    for (int i = 2; i <= N; i++) {
        cin >> p[i];
    }

    vector<vector<int>> G(N + 1);
    for (int i = 2; i <= N; i++) {
        G[p[i]].push_back(i);
    }

    vector<pair<int, int>> insurances(M);
    for (int i = 0; i < M; i++) {
        cin >> insurances[i].first >> insurances[i].second;
    }
    
    sort(insurances.begin(), insurances.end(), [](const pair<int, int> &a, const pair<int, int> &b){
        return a.second > b.second;
    });

    vector<int> covered(N + 1, 0);
    queue<pair<int, int>> q;

    for (auto insurance : insurances) {
        int x = insurance.first;
        int y = insurance.second;

        if (covered[x] < y + 1) {
            covered[x] = y + 1;
            q.push({x, y});
            while (!q.empty()) {
                int v = q.front().first;
                int gen = q.front().second;
                q.pop();
                
                if (gen == 0) {
                    continue;
                }

                for (int nv : G[v]) {
                    if (covered[nv] < gen) {
                        covered[nv] = gen;
                        q.push({nv, gen - 1});
                    }
                }
            }
        }
    }

    cout << count_if(covered.begin(), covered.end(), [](int i) { return i > 0; }) << "\n";

    return 0;
}
