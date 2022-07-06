#include <stdio.h>

int main() {

    int a;
    while(1){
        scanf("%d",&a);
        if(a%3==0){
            printf("%d",a);
            break;
        }
        else if(a%5==0){
            break;
        }
        else{
            printf("No. not divisible by 3 or 5");
        }

    }
    
    return 0;
}
