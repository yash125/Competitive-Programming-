#include<bits/stdc++.h>
#include<iostream>
using namespace std;


int main()
{
    string n;
    cin>>n;
    string m;
    cin>>m;
    int a = n.size();
    int b = m.size();
    
    int dp[n.size()+1][m.size()+1];
    
    for(int i=0;i<=a;i++)
    {
        for(int j=0;j<=b;j++)
        {
            if(i==0)
                dp[i][j] = j;
            
            else if(j==0)
                dp[i][j]=i;
            
            else if(n[i-1]==m[j-1])
                dp[i][j] = dp[i-1][j-1];
            else
                dp[i][j] = 1+ min({dp[i-1][j-1],dp[i][j-1],dp[i-1][j]});
        }
    }
    
    cout<<dp[a][b];
}