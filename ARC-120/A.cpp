#include <iostream>
#include <vector>

using namespace std;
using Int = long long;

int main() {
  Int n;
  cin >> n;
  vector<Int> A;

  for (int i = 0; i < n; i++) {
    Int tmp;
    cin >> tmp;
    A[i] = tmp;
  }

  vector<Int> S(n+1,0);
  for(int i=0;i<n;i++){
    S[i+1]=S[i]+A[i];
  }

  return 0;
}
