'''
	Date: Aug-2-2017
	Author: Shyam Gupta
	Program compares two lists if they are the same
'''

list1 = input("Enter the first list: ")
list2 = input("Enter the second list: ")
length = len(list1)
list1.extend(list2)
index = 0
equality = True
for i in range(length) :
	if(list1[i] == list1[index + length]):
		index += 1	
	else:
		equality = False
		break
if(equality):print "The lists are the same"
else: print "The lists are not the same"