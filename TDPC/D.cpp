#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>

using namespace std;
using Int = long long;

const Int MOD = 1000000007;
const long double PI = 3.141592653589793238462643383279502884L;

map<Int, double> dp[110];

Int gcd(Int a, Int b){
  if(a==0)return b;
  return gcd(b%a,a);
}

Int n,d;

int main(){
  cin>>n>>d;
  dp[0][1] = 1;
  for(int i=0;i<n;i++){
    for(auto [g,p]:dp[i]){
      for(int k=1;k<=6;k++){
        dp[i+1][gcd(g*k,d)] += p/6;
      }
    }
  }
  printf("%.10lf\n",dp[n][d]);
  return 0;
}
