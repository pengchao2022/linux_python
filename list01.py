#!/usr/bin/python3


# To define a list

lt=[]

# Add five numbers to the list

lt += [1, 2, 3, 6, 900, 43]


# To modify the second number in lt with 100

lt[1] = 100

# To add one number in the second location of list

lt.insert(2, 355)


# To delete one number in the first location of list

del lt[1]

#To delete elements from 1 to 3

del lt[1:4]

#To judge lt whether has element 0

print(0 in lt)

#To add element 0 to the lt

lt.append(0)

# To get the index of element 0 in the lt

lt.index(0)

print(lt.index(0))




print(0 in lt)




print(lt)


# To display the length of the list

print(len(lt))


# To display the max element of the list

print(max(lt))


# To clear all the elements in the list

lt.clear()

print(lt)





