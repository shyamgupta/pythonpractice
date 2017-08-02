def findType(userInput):
	if(isinstance(userInput,int)):
		if(userInput>100):print "That's a big number!"
		else: print "That's a small number"
	elif (isinstance(userInput,str)):
		if(len(userInput)>=50):print "Long sentence"
		else: print "Short Sentence"
	else:
		if(len(userInput)>=10):print "Big List"
		else: print "Short List"
userInput = input('Enter an integer, string or a List: ')
findType(userInput)