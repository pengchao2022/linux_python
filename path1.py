#!/usr/bin/python3


import os.path

import time

# this is to print the absulte path of a file

print(os.path.abspath("f1.txt"))


# this is to print the directory name where file located

print(os.path.dirname("f1.txt"))



# this is to check whether the file exist or not

print(os.path.exists("f1.txt"))



# this is to judge the file is exist or not in the location

print(os.path.isfile("f1.txt"))


# this is to judge the dir is exist or not in the location


print(os.path.isdir("f1.txt"))

# this is to get the last time when access the file or directory

print(time.ctime(os.path.getatime("f1.txt")))

# this is to get the last time when modigy the file or directory
t = time.ctime(os.path.getmtime("f1.txt"))

print("standard time is:", t)






# this is to get the create time of file or directory

print(time.ctime(os.path.getctime("f1.txt")))







