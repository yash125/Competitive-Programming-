#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<int> v;
    for(int i=0;i<n;i++)
    {
        int g;
        cin>>g;
        v.push_back(g);
    }
    int sum = 0;
    for(int i=0;i<n;i++)
        sum+=v[i];
    int dp[n+1][sum+1];
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=sum;j++)
        {
            if(j==0)
                dp[i][j]=1;
            else if(i==0)
                dp[i][j]=0;
            else if(j<v[i-1])
                dp[i][j] = dp[i-1][j];
            else
                dp[i][j] = dp[i-1][j]|dp[i-1][j-v[i-1]];
        }
    }
    
    vector<int> ans;
    for(int i=1;i<=sum;i++)
    {
        if(dp[n][i]==1)
            ans.push_back(i);
    }
    cout<<ans.size()<<"\n";
    for(int i: ans)
        cout<<i<<" ";
    
    
    
}