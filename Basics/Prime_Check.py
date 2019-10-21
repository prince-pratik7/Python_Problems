def prime(n):
    if n < 2:
        print(f"{n} is not a prime number")
        return 0

    root = int(n ** 0.5) + 1
    for i in range(2,root):
        if n%i==0:
            print(f"{n} is not a Prime No.")
            return 0
    
    print(f"{n} is a Prime No.")
    return 1

# testing over the first 20 whole numbers
tests = range(21)
for test in tests:
    prime(test)
