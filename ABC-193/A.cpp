#include <iostream>

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  double ans = 1-(double)b/a;
  printf("%.20f",ans*100);
  return 0;
}
