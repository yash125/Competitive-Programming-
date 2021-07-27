#include<bits/stdc++.h>
using namespace std;

int dp[1003][100005];


int Knapsack(vector<int> prices,vector<int> pages,int n,int target)
{
    if(n==0 or target==0)
        return 0;
    if(dp[n][target]!=-1)
        return dp[n][target];
    if(prices[n-1]<=target)
        return dp[n][target] = max(pages[n-1]+Knapsack(prices,pages,n-1,target-prices[n-1]),Knapsack(prices,pages,n-1,target));
    else
        return dp[n][target] = Knapsack(prices,pages,n-1,target);
        
}


int main()
{
    int n,m;
    cin>>n>>m;
    vector<int> prices;
    vector<int> pages;
    for(int i=0;i<n;i++)
    {
        int g;
        cin>>g;
        prices.push_back(g);
    }
    
    for(int i=0;i<n;i++)
    {
        int g;
        cin>>g;
        pages.push_back(g);
    }
    
    for(int i=0;i<=n;i++)
    {
        for(int j=0;j<=m;j++)
        {
            if(i==0 or j==0)
                dp[i][j]=0;
            else if(prices[i-1]<=j)
                dp[i][j] = max(pages[i-1]+dp[i-1][j-prices[i-1]],dp[i-1][j]);
            else
                dp[i][j] = dp[i-1][j];
        }
    }
    
    cout<<dp[n][m];
    
}