import sys
import math
import heapq 
import bisect
import string 
import functools
import itertools
import collections

def allMatch(match,ul):
    for i in ul:
        for j in range(36,1,-1):
            try:
                if(int(i[1],j)==match):
                    break 
            except:
                return False
    return True

def toMatch(kl):
    match=int(kl[0][1],int(kl[0][0]))
    for i in kl[1:]:
        if(match!=int(i[1],int(i[0]))):
            return -1
    return match

def findMatch(ul):
    match=set({})
    for j in range(36,1,-1):
        try:
            match.add(int(ul[0][1],j))
        except:
            break
    for i in ul[1:]:
        temp=set({})
        for j in range(36,1,-1):
            try:
                temp.add(int(i[1],j))
            except:
                break
        match=match.intersection(temp)
        if(len(match)==0):
            return match
    return match
            
t=int(input().strip(" "))
while(t>0):
    n=int(input().strip(" "))
    ul,kl=[],[]
    for i in range(n):
        l=input().strip(" ").split(" ")
        if(l[0]=="-1"):
            ul.append(l)
        else:
            kl.append(l)
    if(len(kl)>=1):
        match=toMatch(kl)
        if(match!=-1 and match<=1000000000000):
            if(allMatch(match, ul)):
                print(match)
            else:
                print(-1)
        else:
            print(-1)
    else:
        match=findMatch(ul)
        if(len(match)!=0 and min(match)<=1000000000000):
            print(min(match))
        else:
            print(-1)
    t=t-1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
