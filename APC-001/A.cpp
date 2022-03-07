#include <iostream>

using namespace std;
using Int = long long;

int main() {
  Int x, y;
  cin >> x >> y;

  if(x%y==0)cout<<-1<<endl;
  else cout<<x<<endl;

  return 0;
}
