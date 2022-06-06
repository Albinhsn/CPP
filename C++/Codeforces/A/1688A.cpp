#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool isPower(int x){
    return (ceil(log2(x)) == floor(log2(x)));
}


int solve(){
    ll x;
    cin >> x;    
    if(x % 2 != 0){
        if(x == 1){
            cout << 3 << "\n";
            return 0;
        }
        cout << 1 << "\n";
        return 0;
    }    
    if(isPower(x) == true){
        cout << x + 1 << "\n";
        return 0;
    }
    
    cout << (ll)pow(2, log2(x & -x)) << "\n";
    return 0;
    
}



int main(){
    int t;
    cin >> t;
    for(int i = 0; i<t; i++){
        solve();
    }
    return 0;
}