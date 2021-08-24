# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

import math

def median(a):
    if a==[]:
        return
    n=len(a)
    a.sort()
    if n%2==0:
        m1=a[n//2]
        m2=a[n//2 - 1]
        median=(m1+m2)/2
    else:
        median=a[n//2]
    return median