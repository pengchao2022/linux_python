#!/usr/bin/python3

d = {"China":"Shanghai", "USA":"Washington", "Japan":"Tokyo", "Korea":"Soule"}

print(len(d))

print(d)

#This is to get a key-value from the dictionary by random

j = d.popitem()

print(j)

m = d["China"]

print(m)

n = d["Japan"]

print(n)

# This is to delete the key and value from dictionary

del d["USA"]

print(d)

# this is to judge the key is in dictionary or not

print("Japan" in d)

print("Germany" in d)

# this is to get all the keys in dictonary

print(d.keys())

# this is to get all the values from the dictionary


print(d.values())

# this is to delete all the keys and values in dictionary

d.clear()

print(d)


