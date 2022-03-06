#include <iostream>

using namespace std;

int main() {
  int x, a, b;
  cin >> x >> a >> b;

  if (-a + b > x) {
    cout << "dangerous" << endl;
  } else {
    if (-a + b <= 0)
      cout << "delicious" << endl;
    else
      cout << "safe" << endl;
  }
  return 0;
}
