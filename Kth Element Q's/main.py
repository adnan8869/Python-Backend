# Problem 1: Kth Largest Element in an Array
import heapq
def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
            
    return heap[0]

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # Output: 4
# Dry RUN:
# 3 -> 3 
# 2 -> 2,3 
# 3 -> 2,3,3 
# 1 -> 1,2,3,3 
# 2 -> 2,2,3,3
# 4 -> 2,3,3,4 
# 5 -> 3,3,4,5
# 5 -> 3,4,5,5 
# 6 -> 4,5,5,6
# heap[0] -> 4

#Problem 2: Kth most repeated elements
from collections import Counter
k=2
lst = Counter([1,1,1,2,2,3])
print(lst.most_common(k))
   
            
