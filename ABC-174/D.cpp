#include <bits/stdc++.h>

using namespace std;

int main()
{

    int N;
    cin >> N;

    string S;
    cin >> S;

    int all_W = count(S.begin(), S.end(), 'W');
    int all_R = count(S.begin(), S.end(), 'R');

    int ans = all_R;

    int left_W = 0;
    int left_R = 0;
    for (int i = 0; i < N; i++)
    {
        if (S[i] == 'W')
            left_W++;
        else
            left_R++;
        int right_R = all_R - left_R;
        ans = min(ans, max(left_W, right_R));
    }
    cout << ans << endl;

    return 0;
}