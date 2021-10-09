#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

// a^n mod を計算する
ll modpow(ll a, ll n, ll mod) {
    ll res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}
 
// a^{-1} mod を計算する
ll modinv(ll a, ll mod) {
    return modpow(a, mod - 2, mod);
}
 
const int MAX = 510000;
const ll MOD = 1000000007;
 
ll fac[MAX], finv[MAX], inv[MAX];
 
// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}
 
// 二項係数計算
ll COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}
int main() {
    ll n, a, b;
    cin >> n >> a >> b;
    COMinit();
    ll v1 = 1;
    for (ll i = n; i > n - a; i--) {
        v1 *= i;
        v1 %= MOD;
    }
    ll v2 = 1;
    for (ll i = n; i > n - b; i--) {
        v2 *= i;
        v2 %= MOD;
    }
    v1 *= finv[a];
    v2 *= finv[b];
    v1 %= MOD;
    v2 %= MOD;
    ll ans = modpow(2, n, MOD) - 1 - v1 - v2;
    ans += 10 * MOD;
    ans %= MOD;
    cout << ans << "\n";
    return 0;
}
