n,m=map(int,input().split())
t=[]
li=[]
for i in range(n):
    li=list(map(int,input().split()))
    t.append(li)
k=int(input())
t2=sorted(t, key = lambda x: int(x[k]))
for i in range(n):
    print(*t2[i])
 
 
'''Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12'''
