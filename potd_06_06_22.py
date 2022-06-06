#Count pairs in array divisible by K 

class Solution(object):
    def countKdivPairs(self, arr, n, k):
        count = [0]*k
        sum_avail = 0
        
        
        for each in (arr):
            mod = each % k
            sum_avail += count[(k-mod)%k]
            count[mod] += 1
        return sum_avail
    
    
#do using hash function