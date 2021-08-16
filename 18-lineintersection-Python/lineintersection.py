# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. 
# If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
    B1=-1
    B2=-1
    A1=m1
    A2=m2
    C1=b1
    C2=b2
    denominator=(A1*B2) - (A2-B1)
    X0= (B1*C2)-(B2*C1)
    Y0= (C1*A2)-(C2*A1)
    if(m1==m2):
        return None
 

