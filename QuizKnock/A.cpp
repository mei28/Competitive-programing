#include <iostream>

using namespace std;

int amount = 3600;
bool check(int x) { return x > amount; }

int main() {
  int a, b, c, d;
  int sum = 0;
  for (a = 1; a < amount / 130 + 10; a++)
    for (b = 1; b < amount / 170 + 10; b++)
      for (c = 1; c < amount / 78 + 10; c++)
        for (d = 1; d < amount / 104 + 10; d++)
          if (a * 130 + b * 170 + c * 78 + d * 104 == amount) {
            cout << b << endl;
            return 0;
          }

  return 0;
}
