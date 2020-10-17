#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() { 
    string s;
    cin >> s;
    int res = 0;
    stack<char> st;
    for (int i = 0;i<s.size();i++){
        if (st.empty()||st.top()==s[i]){
            st.push(s[i]);
        }else{
            res += 2;
            st.pop();
        }
    } 
    cout<<res<<endl;
}