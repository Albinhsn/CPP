#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int A[1500], B[1500];
    for(int i = 0; i<n; i++){
        cin >> A[i];
    }
    for(int i = 0; i < n; i++){
        cout << A[n-i-1] << " ";
    }
    return 0;
}
