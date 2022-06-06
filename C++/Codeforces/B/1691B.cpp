#include <bits/stdc++.h>
#include <map>
typedef long long ll;
using namespace std;

void solve()
{
        
    
    
    int cnt = 0,x, n, prev = INT_MAX;
    cin >> n;        
    vector<int> result;    
    bool flag = false;    
    for(int i = 1; i<=n; i++){        
        cin >> x;                           
        if(prev == INT_MAX){
            prev = x;                
        }            
        else if(x != prev && cnt == 1){
            flag = true;                
            break;
        }else if(x != prev){
            result.push_back(i-1);                
            for(int j = i-cnt; j<i-1; j++){        
                        
                result.push_back(j);
            }                
            prev = x;
            cnt = 0;            
        }
        cnt += 1;            
    }    
    
    if(flag || n == 1 || cnt == 1){
        cout << "-1";
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }else{
        result.push_back(n);

        for (int j = n-cnt+1; j < n; j++)
        {            
            result.push_back(j);
        }
        for(int i = 0; i<n; i++){
            cout << result[i] << " "; 
        }
    }
    cout << "\n";

}

int main()
{
    ios::sync_with_stdio(!cin.tie(0));
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        solve();
    }
}