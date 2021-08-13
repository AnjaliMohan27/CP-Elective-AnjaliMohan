# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def countOccurrences(x, d):
    count = 0 # Initialize count
            # of digit d
    while (x):
        
        # Increment count if current
        # digit is same as d
        if (x % 10 == d):
            count += 1
        x = int(x / 10)

    return count



def mostfrequentdigit(n):
    # Handle negative number
    if (n < 0):
        n = -n
    
    result = 0 # Initialize result
                # which is a digit
    max_count = 1 # Initialize count
                # of result
    
    # Traverse through all digits
    for d in range(10):
        
        # Count occurrences of current digit
        count = countOccurrences(n, d);
        
        # Update max_count and
        # result if needed
        if (count >= max_count):
            max_count = count
            result = d
        
    return result