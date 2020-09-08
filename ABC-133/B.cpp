#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, d;
    cin >> n >> d;

    vector<vector<int>> x(n, vector<int>(d));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < d; j++) {
            cin >> x[i][j];
        }
    }

    int d_int = 0;
    double d_double = 0;
    int count = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = 0; k < d; k++) {
                d_int += (x[i][k] - x[j][k]) * (x[i][k] - x[j][k]);
                d_double += (x[i][k] - x[j][k]) * (x[i][k] - x[j][k]);
            }
            d_int = sqrt(d_int);
            d_double = sqrt(d_double);
            if (d_int == d_double) {
                count++;
            }
            d_int = 0;
            d_double = 0;
        }
    }

    cout << count << endl;
}