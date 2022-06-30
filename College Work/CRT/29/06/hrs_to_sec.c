#include<stdio.h>

int main()
{
    int h,m,s,tot_sec;
    h=5;
    m=30;
    s=55;
    tot_sec=s+(m*60)+(h*3600);
    printf("%d",tot_sec);
}