#include<stdio.h>

int main()
{
    int i,j,n=5;
    for(i=0;i<=5;i++){
        for(j=0;j<=6;j++){
            if((i==0&& j%3!=0)||(i=1&& j%3==0)){
                printf("* ");
            }
            else{
                printf(" ");
            }
        printf("\n");
    }
}

