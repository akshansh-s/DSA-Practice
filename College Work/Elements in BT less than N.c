#include <stdio.h>
 
struct node {
    int data;
    struct node *left;
    struct node *right;
};
 
struct node* getNewNode(int data) {
  struct node* newNode = (struct node*)malloc(sizeof(struct node));
  
  newNode->data = data;
  newNode->left = NULL;
  newNode->right = NULL;
   
  return newNode;
}
 

struct node* generateBTree(){
    // Root Node
    struct node* root =  getNewNode(5);
  
    root->left = getNewNode(-2);
    root->right = getNewNode(8);
  
    root->left->left = getNewNode(12);
    root->left->right = getNewNode(-3);
    root->right->right = getNewNode(2);
  
    root->left->left->left = getNewNode(4);
    root->left->left->right = getNewNode(10);
     
    return root;
 
}

void printSmallerNodes(struct node *nodeptr, int k){
    if(nodeptr != NULL){
        
        printSmallerNodes(nodeptr->left, k);
        
        if(nodeptr->data < k)
           printf("%d ", nodeptr->data);
        
        printSmallerNodes(nodeptr->right, k);
    }
}
int main() {
    struct node *root = generateBTree();    
     
    printf("Nodes Less than 7\n");
    printSmallerNodes(root, 7);
    printf("\nNodes Less than 10\n");
    printSmallerNodes(root, 10);
    getchar();
    return 0; 
}