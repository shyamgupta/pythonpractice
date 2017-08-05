'''
	Date: Aug-4-2017
	Author: Shyam Gupta
	draw_stars() takes a list of integers and prints the number of starts equal to each integer in the list
draw_stars_updated() takes a list of integers & strings - and prints the number of starts equal to each integer in the list, and first letter of the string equal to the length of the string

'''
# Function Definition: draw_stars_()
def draw_stars():
	print 'Running draw_stars()'
	a_list = input("Enter a list of integers: ")
	for i in range(len(a_list)):
		print '*'*a_list[i]
		
# Function Definition: draw_stars_updated()
def draw_stars_updated():
	print 'Running draw_stars_updated()'
	my_list = input("Enter a list of integers and strings: ")
	for i in range(len(my_list)):
		if(isinstance(my_list[i],int)):
			print '*'*my_list[i]
		else:
			print my_list[i][0]*len(my_list[i])


# Function Calls
draw_stars()
draw_stars_updated()

