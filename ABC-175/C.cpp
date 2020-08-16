#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int main()
{
    ll X, K, D;
    cin >> X >> K >> D;
    ll now = X;
    ll left = K;
    ll prev = X;
    ll next_p;
    ll next_m;
    map<ll, ll> mp;
    bool breaked = false;
    ll k = 1;
    for (int i = 0; i < K; i++)
    {
        if (now >= D)
            k = now / D;
        else
            k = 1;
        left -= k;
        prev = now;
        next_p = now + k * D;
        next_m = now - k * D;

        if (abs(next_p) > abs(next_m))
        {
            now = next_m;
        }
        else
        {
            now = next_p;
        }
        mp[now]++;
        if (mp[now] > 1)
        {
            breaked = true;
            break;
        }
        if (left < 0)
            break;
    }
    if (breaked)
    {
        if (left % 2 == 0)
        {
            cout << abs(now) << endl;
        }
        else
        {
            cout << abs(prev) << endl;
        }
    }
    else
    {
        cout << abs(now) << endl;
    }
    return 0;
}