def max_multiple(array):
    A = array
    n = len(A)
    B = []
    A.sort()
    
    start = 0
    end = n-1
    while len(B) < n/2:
        B.append(A[start] * A[end])
        start += 1
        end -= 1
        
    print (A)
    print(B)
    print(max(B))
    
    



array = [-11, 8, 10, 9, -19, -8, 19, -14]
print(max_multiple(array))