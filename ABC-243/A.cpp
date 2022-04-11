#include <iostream>

using namespace std;

int main() {
  int v, a, b, c;
  cin >> v >> a >> b >> c;
  int cnt = 0;
  int A[] = {a, b, c};
  char B[] = {'F', 'M', 'T'};
  while (v >= 0) {
    if (v - A[cnt] < 0)
      cout << B[cnt] << endl;
    v -= A[cnt];
    cnt++;
    cnt %= 3;
  }
  return 0;
}
