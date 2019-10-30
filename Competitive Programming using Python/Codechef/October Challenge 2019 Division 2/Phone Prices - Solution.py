import sys
import math
import heapq 
import bisect
import string 
import operator
import functools
import itertools
import collections


t=int(input().strip(" "))
while(t>0):
    n=int(input().strip(" "))
    l=list(map(int, input().strip(" ").split(" ")))
    l=[math.inf for i in range(5)]+l
    ans=0
    for i in range(5,n+5):
        if(min(l[i-5:i])>l[i]):
            ans+=1
    print(ans)
    t-=1
    
    
    
    
    
    
    
    
    
    
    
    
