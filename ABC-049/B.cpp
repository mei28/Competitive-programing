#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> lines(h);
    for (int i = 0; i < h; ++i) {
        cin >> lines[i];
    }

    for (int i = 0; i < h; i++) {
        string line = lines[i];
        cout << line << endl;
        cout << line << endl;
    }
    return 0;
}