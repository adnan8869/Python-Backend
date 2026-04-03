# def max_subarray_brute(nums):
#     max_sum = float('-inf')
#     for i in range(len(nums)):
#         current_sum = 0
#         for j in range(i, len(nums)):
#             current_sum += nums[j]
#             max_sum = max(max_sum, current_sum)
#     return max_sum

# print(max_subarray_brute([-2,1,-3,4,-1,2,1,-5,4]))


def max_subarray_kadane(nums):
    sum = 0 
    maxi= float('-inf')
    
    for i in range(len(nums)):
        sum += nums[i] 
        maxi = max(maxi, sum)
        if sum < 0:
           sum = 0
         
    return maxi

# Example Output
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum Subarray Sum: {max_subarray_kadane(nums)}") 