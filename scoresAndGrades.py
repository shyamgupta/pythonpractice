import random
def scores():
	print 'Scores and Grades'
	for i in range(10):
		score = random.randint(60,100)
		if(score>=60 and score<70):
			print 'Score: ',score,';','Your grade is D'
		elif(score>=70 and score<80):
			print 'Score: ',score,';','Your grade is C'
		elif(score>=80 and score<90):
			print 'Score: ',score,';','Your grade is B'
		else:
			print 'Score: ',score,';','Your grade is A'
	print 'End of the program. Bye!'
scores()