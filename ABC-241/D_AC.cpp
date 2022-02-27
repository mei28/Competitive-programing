#include<iostream>
#include<set>

using namespace std;
using Int = long long;

Int Q, c, x, k;

int main(){
  cin >> Q;
  multiset<Int> A;
  while(Q--){
    cin >> c;
    if(c == 1){
      cin >> x;
      A.insert(x);      
    }
    if(c == 2){
      cin >> x >> k;
      auto it = A.upper_bound(x);
      while(k > 0 && it != A.begin())k--,it--;
      if(k != 0) cout << -1 << endl;
      else cout << *it << endl;
    }
    if(c == 3){
      cin >> x >> k;
      auto it = A.lower_bound(x);
      k--;
      while(k > 0 && it != A.end())k--,it++;
      if(it == A.end())cout << -1 << endl;
      else cout << *it << endl;
    }
  }
}
