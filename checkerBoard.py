'''
	Date: Aug-2-2017
	Author: Shyam Gupta
	Program prints a checker board
'''
def printboard(value):
	print value*4

for i in range(8):
	if(i%2 == 0):
		printboard('* ')
	else:
		printboard(' *')
