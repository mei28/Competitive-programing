#include <iostream>
#include <string>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    if (a.size() > b.size())
        cout << "GREATER" << endl;
    else if (a.size() < b.size())
        cout << "LESS" << endl;
    else {
        bool flg = false;
        for (int i = 0; i < a.size(); i++) {
            int s, t;
            s = a[i], t = b[i];
            if (s > t) {
                cout << "GREATER" << endl;
                flg = true;
                break;
            } else if (t > s) {
                cout << "LESS" << endl;
                flg = true;
                break;
            }
        }
        if (flg == false) {
            cout << "EQUAL" << endl;
        }
    }
    return 0;
}