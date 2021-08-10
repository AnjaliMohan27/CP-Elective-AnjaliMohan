# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
    num=abs(n)                          #convert the num into positive
    n_list=[int(i) for i in str(num)]   #converting num into list of nums
    if(k==len(n_list)):                 #case-1: if k==len(num_list), just append the d at 
        n_list.insert(0,d)              #the beginning of list
        ans=n_list
    else:                               #case-2: if(len(k)<k), 
        n_list=n_list[::-1]             #reverse the list, a/c to the condition counting starts from right side
        n_list[k]=d                     #replace the kth index with digit "d"
        ans=n_list[::-1]                #and then reverse it to get the initial order
    
    answer=[str(i) for i in ans]        #as we have the ans in the form of list
    answer=int("".join(answer))         #convert it into int
    if(n<0):                            #case-3: if the num 'n' is negative, initially -> return -ve num
        return (-answer)                #else return +ve num
    return (answer)
