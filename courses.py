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









