#include<bits/stdc++.h>
using namespace std;


int  main()
{
    int n;
    cin>>n;
    int arr1[n];
    int element;
    for(int i=0;i<n;i++)
    {
        cin>>element;
        arr1[i]=element;
    }

    int m;
    cin>>m;
    int arr2[m];

    for(int i=0;i<m;i++)
    {
        cin>>element;
        arr2[i] = element;
    }

    int resultantArray[n+m];
    int i=0;
    int j=0;
    int curr=0;
    while(i<n and j<m and curr<(n+m))
    {
        if(arr1[i]<=arr2[j])
        {

            resultantArray[curr] = arr1[i];
            i++;
            curr++;
        }
        else{
            resultantArray[curr] = arr2[j];
            j++;
            curr++;
        }
    }

    while(curr<(n+m) and i<n)
    {
        resultantArray[curr] = arr1[i];
        i++;
        curr++;
    }


    while(curr<(n+m) and j<m)
    {
        resultantArray[curr] = arr2[j];
        j++;
        curr++;
    }

    for(int i=0;i<(n+m);i++)
        cout<<resultantArray[i]<<" ";

}
