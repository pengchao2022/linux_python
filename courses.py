#!/usr/bin/python3



courses = ['History', 'Math', 'Physics', 'CompSci']

courses.append('Art')

courses.insert(0, 'Chemistry')

courses.remove('Physics')

# courses.pop() will remove the last value of a list

courses.pop()

print(courses)

print(courses[0])

print(courses[1])

print(courses[2])

print(courses[3])

print(courses[1:3])

print(courses)

# dismatch the orders from a list

courses.reverse()

print(courses)

# this is to print the index number of one element

print(courses.index('Math'))

courses.append('allen')

print(courses)

print(courses.index('allen'))

# this is to judge the true of false

print('allen' in courses)

print('lily' in courses)

for item in courses:
	
	print(item)







