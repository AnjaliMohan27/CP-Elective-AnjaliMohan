# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.
import math


def fun_nearestodd(n):
	n = math.ceil(n)    #get the ceil value of the given num
	if(n%2 == 0):       #check if it is even, if yes, subtract 1 
		return((n-1))   #as we need the smaller odd, 
	else:
		return(int(n))  #else return the num




