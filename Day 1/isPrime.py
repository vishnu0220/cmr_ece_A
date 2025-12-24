## 3 Prime check
import math as m
# Method 1
def isPrime1(n):
    # check for a factor in between 2 and n-1
    isPrimeNumber = True
    cnt = 0
    for i in range(2, n):
        cnt += 1
        if n % i == 0:
            isPrimeNumber = False
            print("Not a prime")
            break
    if(isPrimeNumber == True):
        print("Prime number")
    print("Got result after ", cnt, " no. of iterations")

# Method 2
def isPrime2(n):
    # check for a factor in between 2 and n/2
    isPrimeNumber = True
    cnt = 0
    for i in range(2, (n//2)+1):
        cnt += 1
        if n % i == 0:
            isPrimeNumber = False
            print("Not a prime")
            break
    if(isPrimeNumber == True):
        print("Prime number")
    print("Got result after ", cnt, " no. of iterations")

# Method 3
def isPrime3(n):
    # check for a factor in between 2 and n/2
    isPrimeNumber = True
    cnt = 0
    for i in range(2, int(m.sqrt(n))+1):
        cnt += 1
        if n % i == 0:
            isPrimeNumber = False
            print("Not a prime")
            break
    if(isPrimeNumber == True):
        print("Prime number")
    print("Got result after ", cnt, " no. of iterations")

n = int(input())
isPrime1(n)
isPrime2(n)
isPrime3(n)
