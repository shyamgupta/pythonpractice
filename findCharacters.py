'''
	Date: Aug-2-2017
	Author: Shyam Gupta
	Program takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

'''
word_list = input("Enter the word list: ")
char = input("Enter an alphabet: ")
new_list = []
for i in word_list:
	if(char in i):new_list.append(i)
print new_list
