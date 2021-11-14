#include <iostream>
#include <vector>

using namespace std;
using Int = long long;

int main(){
    int n, k; cin >> n >> k;
    vector<Int> v(n);
    for(Int &x : v) cin >> x;
    Int ok = 0, ng = 1e18 / k;
    while(ng - ok > 1){
        Int md = (ok + ng) / 2, sum = 0;
        for(Int x : v) sum += min(x, md);
        if(sum >= k * md) ok = md;
        else ng = md;
    }
    cout << ok << endl;
}
