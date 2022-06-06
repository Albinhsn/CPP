#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

void solve(){    
    int a,b,c;
    cin >> a >> b >> c;
    cout << c+b+a << " " << b+c << " " << c << "\n";
    
}



int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for(int i = 0; i<t; i++){
        solve();
    }
}