# Take a number and an integer k as input.
# Write a function to return the k smallest digits from the number in sorted order.


# SOLUTION-1
def sorting(num,k):
   
    digits = list(str(num))
    digits.sort()
    result_digits = digits[:k]
    print("Output:", result_digits)

sorting(437062999, 4)
# Time Complexity : O(n log n) 
# Space Complexity : O(n)


# SOLUTION-2
import heapq
def sorting_fast(num, k):
    digits = list(str(num))
    smallest = heapq.nsmallest(k, digits)
    print("Output:", smallest)

sorting_fast(437062999, 4)
# Time Complexity : O(n log k) 
# Space Complexity : O(n)


# SOLUTION-3
def sorting_fast(num, k):
    count = [0] * 10
    for digit in str(num):
        count[int(digit)] += 1

    result_list = []

    for i in range(10):
        while count[i] > 0 and k > 0:
            result_list.append(str(i))
            count[i] -= 1
            k -= 1
            
        if k == 0:
            break

    return "".join(result_list)
print(sorting_fast(437062999, 4)) 
# Time Complexity : O(n) 
# Space Complexity : O(1)