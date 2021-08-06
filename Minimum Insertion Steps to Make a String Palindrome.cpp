class Solution {
public:
    int minInsertions(string s) {
        
        
        string a ="";
        for(int i=s.size()-1;i>=0;i--)
        {
            a+=s[i];
        }
        
        int dp[505][505];
        int n = s.size();
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=n;j++)
            {
                if(i==0 or j==0)
                    dp[i][j] = 0;
                else if(s[i-1]==a[j-1])
                    dp[i][j] = dp[i-1][j-1]+1;
                else
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }
        }
        
        return n-dp[n][n];


    }
};