#!/usr/bin/python3


f = open("f1.txt", 'rt')

#print(f.readline())

#print(f.read())

print(f.read(2))


# This is to read all the lines in the file

print(f.readlines())

#f = open("f1.txt", 'rb')

#print(f.readline())



f.close()




