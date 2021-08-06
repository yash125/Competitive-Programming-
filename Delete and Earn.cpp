class Solution {
public:
    
    int dp[10005];
    int helper(int ans[],int a)
    {
        if(a==1)
            return ans[1];
        if(a==1 or a==2)
            return max(ans[1],2*ans[2]);
        if(dp[a]!=-1)
            return dp[a];
        return dp[a] = max(helper(ans,a-2)+ans[a]*a,helper(ans,a-1));
    }
    
    
    
    int deleteAndEarn(vector<int>& nums) {
        int a = *max_element(nums.begin(),nums.end());
        int ans[a+1];
        memset(ans,0,sizeof(ans));
        memset(dp,-1,sizeof(dp));
        for(int i: nums)
        {
            ans[i]+=1;
        }
        return helper(ans,a);
    }
};