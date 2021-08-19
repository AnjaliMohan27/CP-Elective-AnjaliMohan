# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
    length = max(len(s1), len(s2))
    output = ""
    i=0
    while(i<length):
        if(i<len(s1)):
            output=output+s1[i]
        if(i<len(s2)):
            output=output+s2[i]
        i=i+1
    return output