#include <iostream>
#include <set>

using namespace std;

int main(){
    set<int> st;
    int l,q;
    cin>>l>>q;

    st.insert(0);
    st.insert(l);
    
    for(int i=0;i<q;i++){
        int c,x;
        cin>>c>>x;
        
        if(c==1){
            st.insert(x);
        }
        else{
            auto it = st.lower_bound(x);
            cout<< *it - *prev(it) <<endl;
        }
    }
    return 0;
}
