#include <iostream>
#include <vector>

using namespace std;



int main(){
  int n,q; cin>>n>>q;
  vector<int> A(n,0);
  for(auto &e: A)cin>>e;
  sort(A.begin(), A.end());
  for(int i=0;i<q;i++){
    int x;cin>>x;
    auto iter = lower_bound(A.begin(),A.end(),x);
    cout<<A.end()-iter<<endl;
  }
  return 0;
}
