 #include <stdio.h>

int main()
{
    int row = 7, col = 7;

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            
        // checking if i < row/2
        if (i < row / 2) {
            
            // checking if j<col/2
            if (j < col / 2) {
                
            // print '*' if j=0
            if (j == 0)
                printf("*");
                
            // else print space
            else
                printf(" ");
                printf(" ");
            }
            
            // check if j=col/2
            else if (j == col / 2)
            printf(" *");
            else
            {
            
            if (i == 0)
                printf(" *");
            }
        }
        else if (i == row / 2)
            printf("* ");
        else {
            
            
            if (j == col / 2 || j == col - 1)
            printf("* ");
            
            // last row
            else if (i == row - 1) {
                
            // last row will be have '*' if
            // j <= col/2 or if it is last column
            if (j <= col / 2 || j == col - 1)
                printf("*");
            else
                printf(" ");
                //printf(" ");
            }
            else
            printf(" ");
            printf(" ");
        }
        }
        printf("\n");
    }
}