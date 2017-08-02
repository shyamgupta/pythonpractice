'''
	Date: Aug-2-2017
	Author: Shyam Gupta
	Program accepts a list comprising of strings & integers.
	Based on the type of each list element, it will print the concatenated string and the sum of integers
'''

def typeList(userInput):
	total = 0
	astring = ''
	int_type = 0
	str_type=0
	for i in userInput:
		if(isinstance(i,int)):
			int_type += 1
			total += i
		else:
			str_type += 1
			astring += ' ' + i
	if int_type>0 and str_type>0:
		print 'The list you entered is of mixed type'
		print 'String: '+ astring
		print 'Sum: ',total
	elif int_type==0:
		print 'The list you entered is of string type'
		print 'String: '+ astring
	else:
		print 'The list you entered is of integer type'
		print 'Sum: ' , total
userInput = input('Enter the list: ')
typeList(userInput)
