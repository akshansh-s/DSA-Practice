#Given a string s, your task is to remove the repeating consecutive characters.

s="jhcdagancjbhgchabhx"
a=[]
for i in range(26):
    a[i]=0
    
for i in len(s):
    a[s[i]]+=1
    
for i in range(26):
    cout<<a[i]