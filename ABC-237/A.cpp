#include <iostream>

using namespace std;
int main() {
  long long n;
  cin >> n;

  long long m = (long long)1 << 31;
  if ((-m <= n) && (n < m))
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
