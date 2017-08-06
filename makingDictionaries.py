'''
	Date: Aug-6-2017
	Author: Shyam Gupta
	Assignment Name: Making Dictionaries
	Program accepts two lists (keys & values) and prints out a dictionary
'''

# Function Definition
def makingDictionaries(keys,values):
	a_dictionary = {}
	for i in range(len(keys)):
		a_dictionary[keys[i]]=values[i]
	print a_dictionary

keys = input('Enter the list of keys: ')
values = input('Enter the list of values: ')
makingDictionaries(keys,values)
	