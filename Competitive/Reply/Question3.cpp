#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,T,K,i,j;
    cin>>T;
    
    for(j=0;j<T;j++)
    {
        cin>>N>>K;
        int A[N],B[N];
        for(i=0;i<N;i++)
           {
               cin>>A[i];
           }
        for(i=0;i<N;i++)
           {
               cin>>B[i];
           }
        sort(A,A+N);
        sort(B,B+N);
        int min=0,max=0;
        for(i=0;i<K;i++)
        {
            min+=A[i]*B[i];
            max+=A[N-i-1]*B[N-i-1];
        }
        cout<<min<<"  "<<max;

    }
    

    return 0;
}

