#! /usr/bin/python

num = int(raw_input("Enter a number:"))
sum = 0
ll = []
pp = 0
for a in range(3,num):
	for x in range(2,a):
		if a%x == 0:
			pp = 0
		else:
			pp = 1
	if pp == 1:
		ll.append(a)
print ll
for y in ll:
	sum = sum + y
print sum
