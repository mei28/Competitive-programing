#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    cin>>s;
    int left,right;
    left=0;
    right=s.size()-1;

    int ans = 0;
    while(right>left){
        if(  s[right] == s[left] ){
            right--;
            left++;
        }else{
            if(  s[right] == 'x' ){
                ans += 1;
                right--;
            }else if(  s[left] == 'x' ){
                ans += 1;
                left++;
            }else{
                ans = -1;
                break;
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}
