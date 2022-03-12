#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> A(n, 0), B(n, 0);
  for (auto &e : A)
    cin >> e;
  for (auto &e : B)
    cin >> e;

  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int a = A[i];
    for (int j = 0; j < n; j++) {
      if (a == B[j])
        cnt++;
    }
  }

  int ans = cnt;
  for (int i = 0; i < n; i++) {
    if (A[i] == B[i])
      ans--;
  }

  cout<<cnt-ans<<endl;
  cout<<ans<<endl;
  return 0;
}
