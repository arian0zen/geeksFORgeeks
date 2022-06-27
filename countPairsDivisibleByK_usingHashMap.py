
def countKdivPairs(arr, n, k):
    hash_map = {}
    ans = 0
    for each in range(len(arr)):
        remainder = arr[each] % k
        if remainder != 0:
            hash_map[((k-remainder) % k)%k] = ans+1
        else:
            ans += hash_map[0]
        hash_map[remainder] = ++1
    print (ans)
    return ans
             
             
             

arr = [2,2,1,7,5,3]
n = 6
k = 4
countKdivPairs(arr, n, k)
    
    
    #unsolved problem #KeyError: 1