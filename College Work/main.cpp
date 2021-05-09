#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
struct Trie{
struct Trie *children[26];
bool isendword;
}*root;
struct Trie *getNode(){
struct Trie *pnode=(struct Trie *)malloc(sizeof(struct Trie));
pnode->isendword=false;
for(int i=0;i<26;i++){
pnode->children[i]=NULL;
}
return pnode;
}
void insert(struct Trie *root,char *s){
struct Trie *p=root;
int i;
int n= strlen(s);
for(i=0;i<n;i++){
int k= s[i]-'a';//index of char
if(!p->children[k]){
p->children[k]=getNode();
}
p=p->children[k];
}
p->isendword=true;
}
bool search(struct Trie *root,const char *s){
struct Trie *p=root;
int i,n=strlen(s);
for(i=0;i<n;i++){
int k= s[i]-'a';//index of char
if(p->children[k]==NULL){
return false;
}
p=p->children[k];
}
return(p!=NULL && p->isendword);
}
int main()
{
struct Trie* root = getNode();
int ch,i,presornot,flag=0;
int x=1,rep=1,sf=1;
char str[10],sstr[10];

FILE *fp;
while(rep!=0){
printf("\nChoose one option from the following list ...\n");
printf("\n===============================================\n");
printf("\n1.Insert in Trie\n2.Search in Trie from txt file::::\n");
scanf("%d",&ch);
switch(ch){
case 1 :
while(x!=0){
printf("\nEnter the string in trie:");
scanf(" %[^\n]%*c", str);
insert(root,str);
printf("\nDo you Want to insert more\nIf Yess Press 1\nIf No Press 0 :");
scanf(" %d",&x);
}
break;
case 2:
fp=fopen("P7.txt","r");
if(fp==NULL)
{
puts("Cannot open file\n");
exit(1);
}
while(fscanf(fp,"%s",str)!=EOF)
{
presornot = search(root,str);
if(presornot==1){
printf("\n%s is present\n",str);
}
else{
printf("\n%s is not present\n ",str);
}
}
break;
}
printf("\nDo you Want Continue \nIf Yess Press 1\nIf No Press 2 : ");
scanf("%d",&rep);
}

return 0;
}