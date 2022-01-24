#include <iostream>
#include <string>

using namespace std;

int main(){
  string S;
  cin >> S;
  int a,b;
  cin>>a>>b;
  a--;
  b--;

  for(int i=0;i<S.length();i++){
    if(i==a)cout<<S[b];
    else if(i==b)cout<<S[a];
    else cout<<S[i];
  }
  cout<<endl;
  return 0;
}
