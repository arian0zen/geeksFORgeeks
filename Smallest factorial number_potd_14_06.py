def find_zeroes(x):
    denominator = 5
    zeroes = 0
    while (x >= denominator):
        zeroes += (x // denominator)
        denominator *= 5
    return zeroes
    
        # print("find_zeroes")
        # return n
    
#setting up the binary search algorithm
def fac_torial(n):
    low = 0
    high = n*5
    factorial = 0 #initializing the factorial number as 0 at first
    while(low<=high):
        #factorial = 0
        mid = (low+high)//2
        #print("mid is:", mid)
        zero = find_zeroes(mid)
        #print ("zeroes are:", zero)
        if zero >= n:
            factorial = mid
            high = mid-1
            #print(factorial)
        else:
            low = mid + 1
            #print(factorial)
        #print("factorial isssss:", factorial)
    #print ("factorial is:", factorial)
    print ("factorial is:",factorial)
    #return factorial
    
#calling the function
fac_torial(8)