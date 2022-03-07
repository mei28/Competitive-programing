#include <iostream>
#include <string>

using namespace std;
int main() {
  string S;
  cin >> S;
  bool c = false;
  bool f = false;

  for (auto e : S) {
    if (e == 'C' && !f)
      c = true;
    if (e == 'F' && c)
      f = true;
  }

  if (c && f)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;
  return 0;
}
