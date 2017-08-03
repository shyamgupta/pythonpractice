'''
	Date: Aug-2-2017
	Author: Shyam Gupta
	Prints whether a number (between 1 to 2000) is even or odd
'''
def evenOdd(limit):
	for i in range(1,limit+1):
		if(i%2 == 0):
			print "Number is "+ str(i) + ". This is an even number."
		else:
			print "Number is "+ str(i) + ". This is an odd number."

evenOdd(2000)