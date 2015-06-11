'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
with open('chipotle.tsv','rU') as f:
    data = [row for row in csv.reader(f, delimiter='\t')]


'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''
header = data[0]
data_body = data[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
from decimal import Decimal
#IF Item Price is the price for each item
#price = [int(row[1]) * Decimal(row[4].strip('$')) for row in data_body]
#average = sum(price)/int(data_body[-1][0])

#IF Item Price is already equal to price*quantity
price_total = [Decimal(row[4].strip('$')) for row in data_body]
average_total = sum(price_total)/int(data_body[-1][0])
 
'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
sodas = [row[3] if "Canned" in row[2] else "" for row in data]
unique_sodas = set(sodas)


'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
# this seems kindof hack but
burrito_toppings = [row[3].count(',') if "Burrito" in row[2] else "" for row in data]
burrito_toppings_only = filter(None, burrito_toppings)
average_toppings = sum(burrito_toppings_only)/len(burrito_toppings_only)

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
# do you mean orders that contain chips? Or the number of times that chips were ordered?

chips_count = [[row[2],row[1]] if "Chips" in row[2] else None for row in data_body]
chips_only = filter(None, chips_count)

from collections import defaultdict

count_chips_dict = defaultdict(list)
for chip_type, quantity in chips_only:
    count_chips_dict[chip_type].append(int(quantity))

final_dict = dict((chip, sum(quantity)) for chip, quantity in count_chips_dict.items())


# if it is ok to use a pivot table:


'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
