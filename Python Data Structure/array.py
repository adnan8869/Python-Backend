# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this



expenses = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
extra_feb_jan = expenses[1] - expenses[0]
print(f"Extra spent in February compared to January: ${extra_feb_jan}")
# 2. Find out your total expense in first quarter (first three months) of the year.
total_first_quarter = sum(expenses[0:3])
print(f"Total expense in first quarter: ${total_first_quarter}")
# 3. Find out if you spent exactly 2000 dollars in any month
# for expense in expenses:
#     if expense == 2000:
#         spent_2000 = True
#         break
# OR
spent_2000 = 2000 in expenses   
print(f"Spent exactly $2000 in any month: {spent_2000}")
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
print(f"Expenses after adding June: {expenses}")
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
expenses[3] -= 200
print(f"Expenses after refund in April: {expenses}")








# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros = ['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
length_heros = len(heros)
print(f"Length of heros list: {length_heros}")
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(f"Heros after adding black panther: {heros}")
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
hulk_index = heros.index('hulk')
heros.insert(hulk_index + 1, 'black panther')
print(f"Heros after moving black panther after hulk: {heros}")
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code. 
heros[heros.index('thor'):heros.index('hulk') + 1] = ['doctor strange']  # Slicing : heros[1:3] = ['doctor strange']
print(f"Heros after replacing thor and hulk with doctor strange: {heros}")
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(f"Heros sorted in alphabetical order: {heros}")





# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number = int(input("Enter a max number: "))
odd_numbers = []
for num in range(1, max_number + 1):
    if num % 2 != 0:
        odd_numbers.append(num)
print(f"Odd numbers between 1 and {max_number}: {odd_numbers}")