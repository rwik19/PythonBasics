from math import sqrt

def main():
    n = int(input("Enter a number: "))
    print(isPrime(n))

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

main()