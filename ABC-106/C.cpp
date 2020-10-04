#include <iostream>
#include <string>

using namespace std;

int main() {
    string S;
    int K;
    cin >> S >> K;
    int inchinum = 0;
    for (int i = 0; i < S.size(); ++i) {
        if (S[i] == '1')
            ++inchinum;
        else
            break;
    }
    if (inchinum >= K)
        cout << 1 << endl;
    else {
        cout << S[inchinum] << endl;
    }
    return 0;
}