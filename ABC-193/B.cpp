#include <iostream>
using namespace std;
const int INF = 0x3fffffff;
void chmin(int& a, int b){ if(a > b) a = b; }

int main(){
    int N;
    cin >> N;
    int ans = INF;
    for(int i = 0; i < N; i++){
        int A, P, X;
        cin >> A >> P >> X;
        if(X > A) chmin(ans, P);
    }
    if(ans == INF) ans = -1;
    cout << ans << endl;
}
