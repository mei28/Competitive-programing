#include "iostream"

using namespace std;

int main() {
  auto calc = [&](long long n) -> long long {
    long long res = 1;
    if (n == 1)
      return res;
    for (long long p = 2; p * p <= n; ++p) {
      res++;
      n /= p;
    }
    if (n > 1)
      res++;
    return res;
  };

  int N;
  cin >> N;
  for (long long n = 1; n <= N; n++)
    cout << calc(n) << " ";
  cout << endl;
  return 0;
}
