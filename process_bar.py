#!/usr/bin/python3

import time

scale = 10

print("============= Process Start =============")

for i in range(scale+1):

    a = '*' * i
	
    b = '.' * (scale -i)

    c = (i/scale)*100

    print("{:^3.0f}%[{}->{}]".format(c,a,b))

    time.sleep(2)


print("============= Process End ==============")


