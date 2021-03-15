#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
using Int = long long;

vector<Int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
Int a[55];
Int bit[55];

int main(){
    int n;
    cin >> n;
    for(int i = 0;i < n;i++){
        cin >> a[i];
        for(int j = 0;j < primes.size();j++){
            if(a[i] % primes[j] == 0)bit[i] |= 1 << j;
        }
    }
    Int ans = 1e18;
    for(int i = 0;i < (1 << primes.size());i++){
        bool ok = true;
        for(int j = 0;j < n;j++){
            if((bit[j] & i) == 0)ok = false;
        }
        if(!ok)continue;
        Int tmp = 1;
        for(int j = 0;j < primes.size();j++){
            if((i >> j) % 2 == 1)tmp *= primes[j];
        }
        ans = min(ans, tmp);
    }
    cout << ans << endl;
    return 0;
}
