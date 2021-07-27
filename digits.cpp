
#include<bits/stdc++.h>
using namespace std;

int dp[8][1000005];
int recur(int n,int X)
{
    if(n==0)
        return 0;
    if(X==0)
        return INT_MAX-1;
    if(dp[X][n]!=-1)
        return dp[X][n];
    string g = to_string(n);
    int a = g[X-1]-'0';
    int ans = n-a;
    string c = to_string(ans);
    if(a!=0)
        return dp[X][n] =  min(1+recur(ans,c.size()),recur(n,X-1));
    else
        return dp[X][n] = recur(n,X-1);
}


int main()
{
    memset(dp,-1,sizeof(dp));
    int n;
    cin>>n;
    string s = to_string(n);
    int a = s.size();
    cout<<recur(n,a);
    
}
