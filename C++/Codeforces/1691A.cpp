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
        //Input the array 
        cin >> n;
        int even = 0, odd = 0;
        for(int j = 0; j<n; j++){            
            cin >> x;
            if(x % 2 == 0){
                even += 1;
            }else{
                odd += 1;
            }
        }
        cout << min(even, odd) << "\n";
        

        //Walk through array,  

    }


    return 0;
}