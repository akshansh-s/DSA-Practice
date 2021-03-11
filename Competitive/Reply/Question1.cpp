// Online C++ compiler to run C++ program online
#include <bits/stdc++.h>
using namespace std;
int NoDivisor(int n)
{
    if(n==1||n==0)
    return 1;
    int count = 2;
    for(int i =2 ;i<=n/2;i++)
    {
        if(n%i==0)
        count++;
    }
    return count;
}

int main() {
    int N,T,HCF,ans,i,j;
    cin>>T;
    
    for(j=0;j<T;j++)
    {
        cin>>N;
        int G[N];
        for(i=0;i<N;i++)
           {
               cin>>G[i];
               if(i==0)
                HCF=G[0];
                else
               HCF=__gcd(G[i],HCF);
           }
    }
    ans=NoDivisor(HCF);
    cout<<ans;

    return 0;
}

