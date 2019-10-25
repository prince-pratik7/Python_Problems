'''
https://en.wikipedia.org/wiki/Fibonacci_number
Prints Fibonacci sequence up to 100.
'''

def fibonacci(n):
    a=0
    b=1
    print(a)
    while b<n :
        print(b)
        temp=b
        b=b+a
        a=temp
        
fibonacci(100)
