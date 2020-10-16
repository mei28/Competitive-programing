#include <bits/stdc++.h>

#define rep(i,n) for (int i = 0; i < (n); ++i)
using namespace std;
using ll = long long;
using P = pair<int,int>;

int main() {
    ll A, B;
    cin >> A >> B;
    int ans = 1;
    ll x = A;
    while(x*2<=B){
        x *= 2;
        ans++;
    }
    cout << ans << endl;
    return 0;
}