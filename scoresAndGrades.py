import random
while(True):
	score = input('Enter score or type quit to exit:  ')
	if(str(score).lower() == 'quit'):
		break
	else:
		if(score>=60 and score<70):
			print 'Grade - D'
		elif(score>=70 and score<80):
			print 'Grade - C'
		elif(score>=80 and score<90):
			print 'Grade - B'
		elif (score>=90 and score<=100):
			print 'Grade - A'
		else:
			print 'Enter a valid input'
