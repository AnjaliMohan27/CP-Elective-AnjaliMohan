# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

import math

def prime(x):
    if (x<2):
        return False
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    maxFactor = round(x**0.5)
    for factor in range(3,maxFactor+1,2):
        if (x % factor == 0):
            return False
    return True

def checkCircular(N) :
     
    #Count digits.
    count = 0
    temp = N
    while (temp > 0) :
        count = count + 1
        temp = temp // 10
         
    num = N;
    while (prime(num)) :
         
        # Following three lines generate the
        # next circular permutation of a
        # number. We move last digit to
        # first position.
        rem = num % 10
        div = num // 10
        num = (int)((math.pow(10, count - 1))
                                * rem)+ div
 
        # If all the permutations are checked
        # and we obtain original number exit
        # from loop.
        if (num == N) :
            return True
     
    return False

def nthcircularprime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (checkCircular(guess)):
            found += 1
    return guess
