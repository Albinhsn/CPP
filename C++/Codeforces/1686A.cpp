#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
    int t, n;
    cin >> t;    
    for(int i = 0; i<t; i++){        
        cin >> n;vector<int> A;
        int sm = 0, x;
        for(int j = 0; j<n; j++){
            cin >> x;
            sm += x;
            A.push_back(x);            
        }
        
        bool flag = false;
        for(int j = 0; j<n; j++){                               
            if(float(sm - A[j]) / float(n-1) == float(A[j]))
            {                
                flag = true;                
                break;                 
            }            
        
        }

        if(flag){
            cout << "YES" << "\n";
        }else{
            cout << "NO" << "\n";
        }
    }    

}