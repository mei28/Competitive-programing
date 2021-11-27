#include <iostream>
#include <string>

using namespace std;

int main() {
  string A, B;
  cin >> A >> B;

  int n = min(A.length(), B.length());
  reverse(A.begin(), A.end());
  reverse(B.begin(), B.end());

  for (int i = 0; i < n; ++i) {
    int a, b;
    a = int(A[i] - '0');
    b = int(B[i] - '0');
    if (a + b >= 10) {
      cout << "Hard" << endl;
      return 0;
    }
  }
  cout << "Easy" << endl;
  return 0;
}
