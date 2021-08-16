# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def mostfrequentdigit(n):
    num_list=[int(i) for i in str(n)]
    n=len(num_list)
    num_list.sort()
    max_count=1
    result=num_list[0]
    current_count=1
    for i in range(1,n):
        if(num_list[i]==num_list[i-1]):
            current_count=current_count+1
        else:
            if(current_count>max_count):
                max_count=current_count
                result=num_list[i-1]
            current_count=1
    if(current_count>max_count):
        max_count=current_count
        result=num_list[n-1]
    return result
