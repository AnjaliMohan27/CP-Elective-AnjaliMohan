# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def isPrime(n): # from course notes
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in range(2,maxFactor+1):
        if (n % factor == 0):
            return False
    return True

def sumOfDigit(n):
    acc = 0
    while(n/10!=0):
        acc += n%10
        n = n/10
    acc += n
    return acc

def isSmithNumber(n):
    if(isPrime(n)): return False
    sumOfFactor = 0
    sumOfNumber = sumOfDigit(n)
    while not(isPrime(n)):
        maxFactor = int(round(n**0.5))
        for factor in range(2, maxFactor+1):
            if(n%factor == 0)and(isPrime(factor)):  #add sum of the digit of factor every loop
                sumOfFactor += sumOfDigit(factor)
                n = n/factor
                break
    sumOfFactor += sumOfDigit(n)
    return (sumOfFactor == sumOfNumber)


def fun_nth_smithnumber(n):
    if(n==0): return 4         #the first one is 4
    i = -1
    x = 4
    while (i<n):
        if(isSmithNumber(x)):   #find the nth smith number
            i += 1
        x += 1
    return x-1