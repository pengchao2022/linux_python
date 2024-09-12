#!/usr/bin/python3


dayfactor = 0.005

dayup = pow(1+dayfactor, 365)

daydown = pow(1-dayfactor, 365)

#print(dayup)

#print(daydown)


print("DayUP: {:.2f}, DayDown: {:.2f}".format(dayup, daydown))

