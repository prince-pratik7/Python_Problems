N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print ('-'*int((M-3*i)/2) +'.|.'*i + '-'*int((M-3*i)/2))
print ('-'*int((M-7)/2)+'WELCOME'+'-'*int((M-7)/2))
for i in range(N-2,-1,-2): 
     print ('-'*int((M-3*i)/2) +'.|.'*i + '-'*int((M-3*i)/2))



 '''Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    '''
