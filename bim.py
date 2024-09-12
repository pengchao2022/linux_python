#!/usr/bin/python3

height, weight = eval(input("Please tyep your height(m) and weight(kg)[, for seperate]:"))

bmi = weight / pow(height, 2)

print("BMI value is:{:.2f}".format(bmi))

who, nat = "", ""

if bmi < 18.5:

	who, nat = "more thin", "more thin"

elif 18.5 <= bmi < 24:

	who, nat = "Normal", "Normal"

elif 24 <= bmi < 25:

	who, nat = "Normal", "more fat"

elif 25 <= bmi < 28:

	who, nat = "more fat", "more fat"

elif 28 <= bmi < 30:

	who, nat = "more fat", "fattest"

else:

	who, nat = "fattest", "fattest"

print("BMI index is: Global'{0}', China'{1}'".format(who,nat))
