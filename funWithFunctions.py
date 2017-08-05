'''
	Date Aug-4-2017
	Author: Shyam Gupta
	Assignment: Python-1, Fun with Functions
'''
# Odd/Even

def oddEven():
	print 'Executing the odd/even function'
	for number in range(2001):
		print 'Number is ',number,'.',
		if(number%2==0):
			print "This is an even number."
		else:
			print "This is an odd number."
oddEven()

#Multiply

def multiply():
	print 'Executing multiply function'
	a_list = input('Enter a list of integers: ')
	for i in range(len(a_list)):
		a_list[i] *= 5
	return a_list
	print a_list

multiply()

#Hacker Challenge

def hackerChallenge(multiply):
	print 'Executing hacker challenge function'
	new_list = []
	a_list = multiply()
	for i in range(len(a_list)):
		for j in range(a_list[i]):
			new_list.append(1)
		a_list[i] = new_list
		new_list=[]
	print a_list
	
	

hackerChallenge(multiply)