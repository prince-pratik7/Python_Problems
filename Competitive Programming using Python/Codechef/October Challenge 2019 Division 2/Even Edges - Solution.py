import sys
import math
import heapq 
import bisect
import string 
import functools
import itertools
import collections
            
            
t=int(sys.stdin.readline())
while(t>0):
    n,m=list(map(int, input().strip(" ").split(" ")))
    deg=dict.fromkeys(list(range(1,n+1)),0)
    for i in range(m):
        x,y=list(map(int, input().strip(" ").split(" ")))
        deg[x],deg[y]=deg[x]+1,deg[y]+1
    if(m%2==0):
        print(1)
        print("1 "*n)
    else:
        flag=0
        for i in deg:
            if(deg[i]%2!=0):
                print(2)
                print("1 "*(i-1)+"2 "+"1 "*(n-i))
                flag=1
                break 
        if(flag==0):
            print(3)
            s=""
            for i in range(1,n+1):
                if(i==x):
                    s=s+"2 "
                elif(i==y):
                    s=s+"3 "
                else:
                    s=s+"1 "
            print(s)
    t=t-1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
