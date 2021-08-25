# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).


def isPrime(x):
    if(x<2):
        return False
    if(x<=3):
        return True
    if(x%2==0 or x%3==0):
        return False
    i=5
    while(i*i<=x):
        if(x%i==0 or x%(i+2)==0):
            return False
        i=i+6
    return True
def carol(x):
    result=(2**x)-1
    return result*result-2

def fun_nth_carolprime(n):
    p,q=0,0
    while(p<=n):
        q+=1
        c=carol(q)
        if(isPrime(c)):
            p+=1
    return c