#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int divisor(int n) {
  vector<int> A;
  for (int i = 1; i * i <= n; i++) {
    if (n % i == 0) {
      A.push_back(n / i);
      if (i * i != n)
        A.push_back(n / i);
    }
  }

  sort(A.begin(), A.end());
  return A.size();
}

int main() {
  int n;
  cin >> n;
  int cnt = 0;
  for (int i = 1; i <= n; i += 2) {
    if (divisor(i) == 8) {
      cnt++;
    }
  }
  cout<<cnt<<endl;
  return 0;
}
