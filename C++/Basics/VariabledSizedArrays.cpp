#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, q, k;
    cin >> n >> q;
    vector<vector<int>> B(n);
    for(int i = 0; i<n; i++){
        cin >> k;
        std::vector<int> A(k);
        for(int j =0; j<k; j++){
            int z;
            cin >> z;
            A[j] = z;
        }
        B[i] = A;
        // for(int j = 0; j<k; j++){
        //     cout << A[j];
        // }
    
    }
    int a, b;
    cout << q;
    for(int i = 0; i<q; i++){
        cin >> a >> b;
        cout << B[a][b] << "\n";
    } 
    return 0;
}
