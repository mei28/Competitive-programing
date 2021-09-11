#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<int> P;
    for(int i=0;i<26;i++){
        int p;
        cin>>p;
        P.push_back(p);
    }
    for(auto v: P){
        cout<<(char)( v+ 'a'-1);
    }
    cout<<endl;
    return 0;
}
