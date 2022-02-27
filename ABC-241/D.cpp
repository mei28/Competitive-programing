#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int q;
  cin >> q;
  vector<int> vec;

  for (int i = 0; i < q; i++) {
    int j, x, k;
    cin >> j;
    if (j == 1) {
      cin >> x;
      vec.insert(upper_bound(vec.begin(), vec.end(), x), x);
    } else {
      cin >> x >> k;
      int idx;
      if (j == 2) {
        idx = distance(vec.begin(), upper_bound(vec.begin(), vec.end(), x));
        if (idx - k < 0) {
          cout << "-1" << endl;
        } else {
          cout << vec[idx - k] << endl;
        }
      } else if (j == 3) {
        idx = distance(vec.begin(), lower_bound(vec.begin(), vec.end(), x));
        if (idx + k > vec.size()) {
          cout << "-1" << endl;
        } else {
          cout << vec[idx + k - 1] << endl;
        }
      }
    }
  }

  return 0;
}
