### Homework exercise
1. Using `chipotle.tsv` in the `data` subdirectory:
    1. `head chipotle.tsv`
	The data is describing chipotle orders. Each row contains informaiton ababout each distinct item in each order. Columns: (if blank, then assume column_name = description). 
		* order_id = id given to each order
		* quantity = for each item in the order, the number of items
		* item_name
		* choice_description = customer preferences for each item 
		* item_price
    2. How many orders are in the data?    
	`tail chipotle.tsv`    
	1834 orders
    3. How many lines are in the data?    
	`wc chipotle.tst`    
	4623 lines
    4. Which burrito is more popular, steak or chicken?    
		`grep -i 'steak burrito' chipotle.tsv | wc`    
		368    
		`grep -i 'chicken burrito' chipotle.tsv | wc`    
		553    
		
		`grep -i 'chicken burrito' chipotle.tsv > chicken_burrito.tsv`    
		`grep -i 'steak burrito' chipotle.tsv > steak_burrito.tsv`

		`cat chicken_burrito.tsv | awk '{ sum += $2 } END { print sum }'`    
		591    
		`cat steak_burrito.tsv | awk '{ sum += $2 } END { print sum }'`    
		386

		Chick burritos are in more orders than steak.
		Chick burritos are ordered more than steak.
    5. Do chicken burritos more often have black beans or pinto beans?    
		`grep -i 'black beans' chicken_burrito.tsv | wc`    
		282    
		`grep -i 'pinto beans' chicken_burrito.tsv | wc`    
		105  
	
		Black Beans

2. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.
 
	The following is throwing a permission denied error:
	`find / . -name chipotle.tsv`    
	The following is throwing a no such file error:
	`find / -name *.*sv`    
	Would love to know the correct way to accomplish this on a mac.


3. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.
`grep -i -r 'dictionary' . | wc`    
17

4. **Optional:** Use the the command line to discover something "interesting" about the Chipotle data. The advanced commands below may be helpful to you
