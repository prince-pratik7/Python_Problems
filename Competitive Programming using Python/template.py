import sys
import math
import heapq
import bisect
import string
import functools
import itertools
import collections

# A recursive solution for subset sum
# problem
# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(n, sumv) :
    global arr

    # Base Cases
    if (sumv == 0) :
        return True
    if (n == 0 and sumv != 0) :
        return False

    # If last element is greater than
    # sum, then ignore it
    if (arr[n - 1] > sumv) :
        return isSubsetSum(n - 1, sumv)
    else:
        # else, check if sum can be obtained
        # by any of the following
        # (a) including the last element
        # (b) excluding the last element
        return isSubsetSum(n-1, sumv) or isSubsetSum(n-1, sumv-arr[n-1])


def isPrime(n) :
    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True


# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print p,

# Simple DFS definition
def dfs(u):
    global visited,n,m,d,ce
    visited[u],ce=True,((ce)%M+1)%M
    if(d[u]==tuple([])):
        return
    else:
        for i in d[u]:
            if(not visited[i]):
                dfs(i)
        return


t=int(sys.stdin.readline())
while(t>0):
    n=int(sys.stdin.readline())
    l=list(map(int, sys.stdin.readline().strip(" ").split(" ")))
    ans=0
    #Write your logic here
    sys.stdout.write(str(ans))
    t=t-1
