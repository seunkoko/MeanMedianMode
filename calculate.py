#A program to calculate the mean, median and mode of a list of numbers.

list = []
dict = {}

times = input("How many numbers do you want to add?:")

while (times != 0):
	number = input("Enter a number in the set: ")
	list.append(number)
	times -= 1
else:
	pass
	
#We calculate mean now
if len(list) == 0:
	print "You have entered an empty set."
else:
	list.sort()
	total = 0
	denom = len(list)
	for items in list:
		total += items
	mean = float(total)/float(denom)
	
	if denom % 2 == 0:
		firstIndex=denom/2
		secondIndex = firstIndex - 1
		
		median = float(list[firstIndex] + list[secondIndex])
		median = median/2
	else:
		median = (denom - 1)/2    
		median = list[median]
		
	for items in list:
		
		high = ""
		for item in list:
			
		
	dict["mean"] = mean
	dict["median"] = median
	dict["mode"] = 0
	
	print
	print dict
	
		

