# Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print 'Executing Part 1 of Assignment'
for i in range(len(students)):
	for key in students[i]:
		print students[i][key],
	print('\n')	
	
# Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print 'Executing Part 2 of the Assignment'
for key in users:
	print key
	for i in range(len(users[key])):
		print i+1 , ' - ',
		sum =0
		for k in users[key][i]:
			print users[key][i][k],
			sum += len(users[key][i][k])
		print ' - ',sum,	
		print('\n')