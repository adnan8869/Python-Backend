# # reverse a string
# def reverse_string(s):
#     return s[::-1]  
# # example usage
# test_string = "Hello, World!"
# print("Original String:", test_string)
# print("Reversed String:", reverse_string(test_string))



# #check string is palindrome or not
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False


# # find factorial of a number
# def factorial_best(n):
#     if n < 0: 
#         return None # Factorials don't exist for negatives
#     res = 1
#     for i in range(2, n + 1): # Start at 2 because multiplying by 1 changes nothing
#         res *= i
#     return res
# print(factorial_best(5))  # 120
# print(factorial_best(0))  # 1


# #check number of prime numbers in a given range
# def is_prime(num):
#     if num < 2:
#         return False
    
#     # Check if any number from 2 up to num-1 divides it
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
            
#     return True

# # The range you want to check
# for n in range(10, 51):
#     if is_prime(n):
#         print(n, end=" ") 
# # Output: 11 13 17 19 23 29 31 37 41 43 47



#Check Armstrong number
# def is_armstrong_math(num):
#     original_num = num
#     num_digits = len(str(num)) # You still need the count of digits
#     total = 0
    
#     temp = num
#     while temp > 0:
#         digit = temp % 10          # Get the last digit
#         total += digit ** num_digits
#         temp //= 10                # Remove the last digit
        
#     return total == original_num

# # Test
# print(is_armstrong_math(153))  # True
# print(is_armstrong_math(9474)) # True (9^4 + 4^4 + 7^4 + 4^4 = 9474)
# print(is_armstrong_math(123))  # False




# # Find GCD of two numbers
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(48, 18))  # 6
# print(gcd(101, 10))  # 1

# # Find LCM of two numbers
# def find_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def find_lcm(a, b):
#     if a == 0 or b == 0:
#         return 0
#     # Use the formula: (a * b) // GCD
#     return abs(a * b) // find_gcd(a, b)

# print(find_lcm(12, 18)) # Output: 36

# # Fibonacci series up to n terms
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series


# print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# # Find sum of digits of a number
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
# print(sum_of_digits(1234))  # 10
# print(sum_of_digits(0))     # 0

# #check the count of occurrences of a character in a string
# text = "banana"
# counts = {}

# for char in text:
#     counts[char] = counts.get(char, 0) + 1

# print(counts)
# # Output: {'b': 1, 'a': 3, 'n': 2}


# # Find largest element in a list
# def find_largest(nums):
#     # Assume the first number is the largest
#     largest = nums[0]
    
#     for n in nums:
#         if n > largest:
#             # If we find a bigger number, update the 'largest' variable
#             largest = n
            
#     return largest

# numbers = [10, 45, 2, 99, 105, 7]
# print(find_largest(numbers)) # Output: 105




# # # Find smallest element in a list
# # def find_smallest(lst):
# #     if not lst:
# #         return None
# #     smallest = lst[0]
# #     for num in lst:
# #         if num < smallest:
# #             smallest = num
# #     return smallest 
# # print(find_smallest([3, 1, 4, 1, 5, 9, 2, 6]))  # 1
# # print(find_smallest([]))  # None



# # #sum of all elements in a list
# # def sum_of_list(lst):
# #     return sum(lst)
# # print(sum_of_list([1, 2, 3, 4, 5]))  # 15
# # print(sum_of_list([]))  # 0



# # Find second largest element in a list
# def get_second_largest(nums):
#     if len(nums) < 2:
#         return None

#     largest = float('-inf')
#     second_largest = float('-inf')

#     for n in nums:
#         if n > largest:
#             # Current largest becomes second, new number becomes largest
#             second_largest = largest
#             largest = n
#         elif n > second_largest and n != largest:
#             # New number is better than silver but not gold
#             second_largest = n

#     return second_largest if second_largest != float('-inf') else None

# numbers = [10, 20, 4, 45, 99, 99, 45]
# print(get_second_largest(numbers)) # Output: 45




# #Find pairs in a list whose sum is equal to a given number
def find_pairs(nums, target):
    seen = set()
    pairs = []
    
    for num in nums:
        complement = target - num  # What number do we need?
        
        if complement in seen:
            pairs.append((complement, num))
        
        seen.add(num)  # Remember this number for later
        
    return pairs

numbers = [2, 4, 3, 5, 7, 8, 9]
target_sum = 7
print(find_pairs(numbers, target_sum)) 
# Output: [(3, 4), (2, 5)]



# # Remove duplicates from a list
# def remove_duplicates(lst):
#     return list(set(lst))
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
# print(remove_duplicates([]))  # []
