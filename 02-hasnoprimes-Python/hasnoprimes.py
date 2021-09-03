# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True  

def fun_hasnoprimes(l):
    result=False
    for i in range(len(l)):
	    for j in range(len(l[i])):
		    result=test_prime(l[i][j])
    if(result==False):
        return True
    else:
        return False
