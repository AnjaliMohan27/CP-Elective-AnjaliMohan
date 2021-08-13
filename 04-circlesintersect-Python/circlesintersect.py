# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

#c1c2 = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )

#If C1C2 > R1 + R2
#      Circle A and B are not touch to each other.
# If C1C2 < R1 + R2
#       Circle intersects each other.

import math

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
    c1c2=int(math.sqrt( (x1-x2)**2 + (y1-y2)**2 ))
    d=(r1+r2)
    if(c1c2<=d):
        return True
    else:
        return False
