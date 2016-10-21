#!/usr/bin/python
sum = 0
for x in range(101):
    if x%11 != 0 and x%10 != 0:
        print x
    sum = sum + x
print sum

l = [1,2,3,4]	
num = 0
for x in l:
	for y in l:
		for z in l:
			for m in l:
				if x != y and y != z and x != z and z != m and x != m and y != m:
					print x,y,z,m
					num = num + 1
print "Total is",num
