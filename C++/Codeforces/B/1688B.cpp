#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int solve(){
    int n;    
    cin >> n;

    int evenCount = 0;
    int lowest = INT_MAX;
    bool odd = false;
    for(int i = 0; i<n; i++){
        int x;
        cin >> x;
        if(!odd && x%2 != 0){
            odd = true;
        }else if(x%2 == 0){
            evenCount += 1;
            int cnt = 0;
            while(x % 2 == 0 && cnt < lowest){                
                cnt += 1;
                x /= 2;
            }
            if(cnt < lowest){
                lowest = cnt;
            }
        }
        
        
    }
    
    // cout << lowest << " " << evenCount << " " << odd << "\n";
    if(evenCount == 0){
        cout << 0 << "\n";
        return 0;
    }
    if(odd){
        cout << evenCount << "\n";
        return 0;
    }
    cout << lowest + evenCount - 1 << "\n"; 
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

