#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using P = pair<ll, ll>;

const ll dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};
const ll ll_inf = ll(1e9) * ll(1e9);

#define REP(i, n) for (ll i = 0; i < (ll)(n); ++i)

int main()
{
    ll H, W;
    cin >> H >> W;
    ll startX, startY, endX, endY;
    cin >> startX >> startY >> endX >> endY;
    startX--, endX--, startY--, endY--;

    vector<vector<char>> s(H, vector<char>(W));
    REP(i, H)
    REP(j, W)
    cin >> s[i][j];

    // 魔法を使った回数
    vector<vector<ll>> cnts(H, vector<ll>(W, ll_inf));
    queue<P> q, visited;
    q.push(P(startX, startY));
    cnts[startX][startY] = 0;

    while (!q.empty() || !visited.empty())
    {
        ll nowX, nowY;
        if (!q.empty())
        {
            nowX = q.front().first;
            nowY = q.front().second;

            visited.push(P(nowX, nowY));
            q.pop();
            REP(i, 4)
            {
                ll nextX = nowX + dx[i];
                ll nextY = nowY + dy[i];
                if (0 <= nextX && nextX <= H - 1 && 0 <= nextY && nextY <= W - 1)
                {
                    if (s[nextX][nextY] == '#')
                        continue;
                    if (cnts[nowX][nowY] < cnts[nextX][nextY])
                    {
                        cnts[nextX][nextY] = cnts[nowX][nowY];
                        q.push(P(nextX, nextY));
                    }
                }
            }
        }
        else
        {
            nowX = visited.front().first, nowY = visited.front().second;
            visited.pop();
            for (ll ix = -2; ix <= 2; ++ix)
            {
                for (ll iy = -2; iy <= 2; ++iy)
                {
                    ll nextX = nowX + ix, nextY = nowY + iy;
                    if (0 <= nextX && nextX <= H - 1 && 0 <= nextY && nextY <= W - 1)
                    {
                        if (s[nextX][nextY] == '#')
                            continue;
                        if (cnts[nowX][nowY] + 1 < cnts[nextX][nextY])
                        {
                            cnts[nextX][nextY] = cnts[nowX][nowY] + 1;
                            q.push(P(nextX, nextY));
                        }
                    }
                }
            }
        }
    }

    if (cnts[endX][endY] == ll_inf)
    {
        cout << -1 << '\n';
    }
    else
    {
        cout << cnts[endX][endY] << '\n';
    }
    return 0;
}