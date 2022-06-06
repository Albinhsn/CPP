#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
    int t, n, x;
    cin >> t;
    for(int i = 0; i<t; i++){        
        cin >> n; 
        bool flag = false;
        int cnt = 0, last = -1;
        for(int j = 0; j<n;j++){
            cin >> x;
            if(!flag && x < last && last != -1){                
                cnt += 1;
                flag = true;
                last = x;
            }
            else{
                flag = false;
                last = x;
            }
        }
        cout << cnt << "\n";

    }    
   

    return 0;
}