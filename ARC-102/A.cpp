#include <iostream>

using namespace std;

int main(){
    long long n,k ;
    cin>>n>>k;
    if(k%2==0){
        long long a = n/k;
        long long b = (n+(k/2))/k;
        cout<<a*a*a + b*b*b <<endl;
    }
    else{
        long long a = n/k;
        cout<<a*a*a <<endl;
    }

}
