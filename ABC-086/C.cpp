#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <functional>
#include <vector>     // std::vector
using namespace std;

int main(void){
    int N, t, x, y, i, t_before, x_before, y_before, flag = 1;
    scanf("%d", &N);
    t_before = x_before = y_before = 0;
    for (i=0; i<N; i++) {
        scanf("%d %d %d", &t, &x, &y);
        if( (t - t_before) < (abs(x - x_before) + abs(y - y_before)) ){
            flag = 0;
            break;
        }
        if( (t - t_before) >= (abs(x - x_before) + abs(y - y_before))  && ( (t - t_before) - (abs(x - x_before) + abs(y - y_before)) ) % 2 == 1 ){
            flag = 0;
            break;
        }
        t_before = t; x_before = x; y_before = y;
    }
    if(flag == 1){cout << "Yes" << endl;}
    else{cout << "No" << endl;}
}