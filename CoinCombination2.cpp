#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,target;
    cin>>n>>target;
    vector<int> v;
    for(int i=0;i<n;i++)
    {
        int g;
        cin>>g;
        v.push_back(g);
    }
    
    int dp[n+1][target+1];
    
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=target;j++)
        {
            if(j==0)
                dp[i][j]=1;
            else if(i==0)
                dp[i][j]=0;
            else if(v[i-1]<=j)
                dp[i][j] = (dp[i][j-v[i-1]]+dp[i-1][j])%1000000007;
            else
                dp[i][j] = dp[i-1][j]%1000000007;
        }
    }
    
    cout<<dp[n][target];
}

