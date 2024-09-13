#!/usr/bin/python3

A = set("Hellokitty20242028")

print(A)


# Add element x to the colletion A

A.add('x')

print(A)

# To judge whether x is in the colletion A or not

print( 'x' in A)

A.add('M')

print(A)

# To remove the element 'M'

A.discard('M')

print(A)

print('M' in A)

# To remove element if element does not exist , then will get keyError 

#A.remove('N')

#print(A)

Z = A.pop()

print("Z is:", Z)

# To clear the collection

A.clear()

print(A)



