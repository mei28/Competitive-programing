#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, q;

const int INF = (1 << 29);
vector<int> G[1 << 18];
int dist[1 << 18];
vector<vector<int> > diff_all(10010, vector<int>(10010));

void getdist(int start) {
    for (int i = 1; i <= n; i++) {
        dist[i] = INF;
    }

    queue<int> Q;
    Q.push(start);
    dist[start] = 0;

    while (!Q.empty()) {
        int pos = Q.front();
        Q.pop();
        for (int to : G[pos]) {
            if (dist[to] == INF) {
                dist[to] = dist[pos] + 1;
                Q.push(to);
            }
        }
    }
}

int main() {
    cin >> n >> q;
    cout << n << endl;
    int a, b;
    for (int i = 1; i <= n - 1; i++) {
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    for (int i = 1; i <= n; i++) {
        getdist(i);
        for (int j = 1; j <= n; j++) {
            diff_all[i][j] = dist[j];
        }
    }

    for (int i = 0; i < q; i++) {
        int c, d;
        cin >> c >> d;

        int diff = diff_all[c][d];
        if (diff % 2 == 0) {
            cout << "Town" << endl;
        } else {
            cout << "Road" << endl;
        }
    }
    return 0;
}