# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
    a=sorted(a)
    if(a==[]):
        return -1
    if(len(a)<=2):
        return abs(a[0]-a[1])

    min_diff=abs(a[1]-a[0])
    n=len(a)
    for i in range(2,n):
        min_diff=min(min_diff, a[i]-a[i-1])
    return min_diff
