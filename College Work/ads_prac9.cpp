#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100

#define initial 1
#define visited 2
#define finished 3

int n;   
int adj[MAX][MAX];
void create_graph( );

int state[MAX];

void DF_Traversal();
void DFS(int v);

int main()
{
        create_graph();
        DF_Traversal();
        return 0;
}

void DF_Traversal()
{
        int v;

        for(v=0; v<n; v++)
                state[v] = initial;

        DFS(0);

        for(v=0; v<n; v++)
        {
                if(state[v]==initial)
                        DFS(v);
        }
        printf("\nGraph is Acyclic\n");
}

void DFS(int v)
{
        int i;
        state[v] = visited;

        for(i=0; i<n; i++)
        {
                if(adj[v][i]==1)
                {
                        if(state[i]==initial)
                                DFS(i);
                        else if(state[i]==visited)
                        {
                                printf("\nBack edge  (%d,%d) found\n", v, i);
                                printf("\nGraph is cyclic\n");
                                exit(1);
                        }
                }
        }
        state[v] = finished;
}

void create_graph()
{
    int i=0, j;
    int a[50];
    int k;
    FILE *fp;
    fp = fopen("matrix.txt","r");
    if(fp == NULL)
    {
        printf("\n\t\tFile Opening Error \n ");
        exit(0);
    }
    else
    {
        while(fscanf(fp,"%d\t",&a[i])!=EOF)
        {
            printf("%d\t",a[i]);
            i++;
        }
    }
    n = sqrt(i+1);
    printf("\n\t\tNo. of Vertices in Graph are  :  %d \n\n",n);
    k = 0;

    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            adj[i][j] = a[k];
            k++;
        }
    }
    printf("\n\t\t*Adjacency Matrix*\n\n");

    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            printf("%d\t",adj[i][j]);
        }
        printf("\n");
    }
        
}