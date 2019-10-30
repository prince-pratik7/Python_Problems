import time

def checkPrime(n):
    if n < 2:
        print(f"{n} is not a prime number")
        return False

    root = int(n ** 0.5) + 1
    for i in range(2,root):
        if n%i==0:
            print(f"{n} is not a Prime No.")
            return False

    print(f"{n} is a Prime No.")
    return True

# Based on the idea that all the primes are of form (6*k +- 1) and a number can be expressed in it's prime factors
def checkPrimeModified(n) :

    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :  #Trying to divide the number using possible prime factors
            return False
        i = i + 6

    return True

n=int(input("Enter Upper Limit: ").strip(" "))
tests = range(n+1)

print("Using checkPrime()Method")
for test in tests:
    checkPrime(test)

print("Using checkPrimeModified() Method")
for test in tests:
    if(checkPrimeModified(test)):
        print(test, "is a Prime Number", sep=" ")
    else:
        print(test, "is a not Prime Number", sep=" ")
