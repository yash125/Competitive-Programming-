#include<bits/stdc++.h>
using namespace std;

int main()
{
    string n;
    string m;
    
    cin>>n;
    cin>>m;
    int c=0;
    
    for(int i=0;i<n.size();i++)
    {
        if(n[i]!=m[i])
            c++;
    }
    
    
    if(c%2==1)
        cout<<"impossible";
    else
    {
        int left=c/2;
        int right=c/2;
        string ans="";
        for(int i=0;i<n.size();i++)
        {
            if(n[i]==m[i])
                ans+=n[i];
            else
            {
                if(left>0)
                {
                    left--;
                    ans+=n[i];
                }
                else if(right>0)
                {
                    right--;
                    ans+=m[i];
                }
            }
        }
        cout<<ans;
    }
}