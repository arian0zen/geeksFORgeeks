'''
Given an array of n elements, where each element is at most k away from its target position, you need to sort the array optimally.

Example 1:

Input:
n = 7, k = 3
arr[] = {6,5,3,2,8,10,9}
Output: 2 3 5 6 8 9 10
Explanation: The sorted array will be
2 3 5 6 8 9 10
'''

from ctypes.wintypes import HWINSTA
import heapq
from traceback import print_tb


def sortedArray(array, k): #arr is array, where each element is at most k away from its target position where it can be sorted
    length = len(array)
    
    heapArray = array[:k]
    heapq.heapify(heapArray)
    #print (heapArray)
    result = []
        
    for element in arr[k:]:
        heapq.heappush(heapArray, element)
        result.append(heapq.heappop(heapArray))
    while heapArray:
        result.append(heapq.heappop(heapArray))
    print ("sorted array: ",result)
    
    #heapArray = array
    #heapq.heapify(heapArray)
    #print (heapArray)
    #heapq.heappush(heapArray, k)
    #print (heapArray)
    #heapq.heappop(heapArray)
    #print (heapArray)
    
arr= [6,5,3,2,8,10,9]
sortedArray(arr, 3)







'''
f = heapq.heapify(arr)

# printing created heap
print ("The created heap is : ",end="")
print (list(f))
'''