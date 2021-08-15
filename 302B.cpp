#include<bits/stdc++.h>
using namespace std;
 
int main()
{
    int n,m;
    cin>>n>>m;
    vector<int> v(n);
    vector<int> queries;
    
    
    int c=0;
    for(int i=0;i<n;i++)
    {
        int g,h;
        cin>>g>>h;
        c+=g*h;
        v[i] = c;
    }
    
    for(int i=0;i<m;i++)
    {
        int g;
        cin>>g;
        auto l = std::lower_bound(v.begin(),v.end(),g);
        std::cout << l-v.begin()+1 << std::endl;
        
    }
    
    
}