# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
    ans=""
    if(a>b and a>c):
        ans=ans+str(a)
        if(b>c):
            ans=ans+str(b)+str(c)
        else:
            ans=ans+str(c)+str(b)
    elif(b>a and b>c):
        ans=ans+str(b)
        if(a>c):
            ans=ans+str(a)+str(c)
        else:
            ans=ans+str(c)+str(a)
    else:
        ans=ans+str(c)
        if(a>b):
            ans=ans+str(a)+str(b)
        else:
            ans=ans+str(b)+str(a)    
    return int(ans)    

