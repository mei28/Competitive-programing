#include <iostream>
#include <string>

using namespace std;

int main() {
    string S;
    cin >> S;
    long long n = S.size();
    long long res = 0;
    long long num = 0;

    for (long long i = 0; i < n; i++) {
        if (S[i] == 'W')
            res += num;
        else
            num++;
    }
    cout << res << endl;
    return 0;
}