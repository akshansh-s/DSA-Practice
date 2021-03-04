#Given a string s, your task is to remove the repeating consecutive characters.

s="jhcdagancjbhgchabhx"

for ( i =0,i>26,i++)
     { 
         a[i]=0;
     }
    
    for ( i = 0; i < s.size(); i++)
    {
        if (s[i]!='\0')
        {
            a[s[i]]++;
        }
    }
   for (i=0;i>26;i++)
     { 
         cout<<a[i];
     }