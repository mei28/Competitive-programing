#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> A;
  vector<int> dct(n+1,0);

  for(int i=0;i<4*n-1;i++){
    int a;
    cin>>a;
    dct[a]++;
  }

  for(int i=0;i<=n;++i){
    if(dct[i]==3){
      cout<<i<<endl;
    }
  }
  return 0;
}
