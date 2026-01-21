# Want to use stocks_prices.csv file for this code example.
# Find price for the specific date.

stocks_prices = []
with open('stock_prices.csv','r') as file:
    for line in file:
        # print(line)
        day,price = line.split(',')
        stocks_prices.append((day, float(price)))

    for day, price in stocks_prices:
        if day == '9-Mar':
            print(f'Stock price on {day} is {price}')
# This List approach is less efficient(because of O(n) time complexity for lookups) 






# This Dictionary approach is more efficient(because of O(1) time complexity for lookups) 
stocks_prices = {}
with open('stock_prices.csv','r') as file:
    for line in file:
        # print(line)
        day,price = line.split(',')
        stocks_prices[day] = float(price)

    if '9-Mar' in stocks_prices:
        print(f'Stock price on 9-Mar is {stocks_prices["9-Mar"]}')