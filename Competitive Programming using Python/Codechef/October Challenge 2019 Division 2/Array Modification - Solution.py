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
    n,k=list(map(int, input().strip(" ").split(" ")))
    l=list(map(int, input().strip(" ").split(" ")))
    ansl=[]
    for i in range(1,n+1):
        if(i<=k):
            c=int(math.floor((k-i)/n))+1
            if(i<=n-i+1):
                if(c%3==0):
                    ansl.append(l[i-1])
                elif(c%3==1):
                    ansl.append(l[i-1]^l[n-i])
                else:
                    ansl.append(l[n-i])
            else:
                if(c%3==0):
                    ansl.append(l[i-1])
                elif(c%3==1):
                    ansl.append(l[n-i])
                else:
                    ansl.append(l[n-i]^l[i-1])
        else:
            ansl.append(l[i-1])
    if(n%2!=0 and n//2+1<=k):
        ansl[n//2]=0
    for i in ansl:
        print(i,end=" ")
    print()
    t=t-1 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    