# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    n=abs(n)
    prevDigit=-1
    while(n>0):
        onesDigit=n%10
        n=n//10
        if(prevDigit==onesDigit):
            return True
        prevDigit=onesDigit
    return False
