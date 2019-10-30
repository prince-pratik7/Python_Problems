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
    n,m,q=list(map(int, input().strip(" ").split(" ")))
    rlist=[0]*n
    clist=[0]*m 
    while(q>0):
        x,y=list(map(int, input().strip(" ").split(" ")))
        rlist[x-1],clist[y-1]=rlist[x-1]+1,clist[y-1]+1
        q-=1 
    orc,erc,occ,ecc=0,0,0,0
    for i in rlist:
        if(i%2==0):
            erc+=1 
        else:
            orc+=1
    for i in clist:
        if(i%2==0):
            ecc+=1 
        else:
            occ+=1
    print(erc*occ+orc*ecc)
    t=t-1
    
    
    
    
    
    
    
    
    
    
    
    