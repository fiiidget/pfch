

def average(list_of_things):

	total_number_of_things = len(list_of_things)

	total_value = 0

	for x in list_of_things:
		try:
			total_value = total_value + x
		except:
			continue


	results = total_value / total_number_of_things
	return results


#calling the function

my_numbers = ["asdfasdf","asdfasdf","asdfas"]

my_results = average(my_numbers)

print(my_results)



