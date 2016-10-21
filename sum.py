#! /usr/bin/python

m = 0 
sum = 0
num = 1

while num <= 100:
	sum = sum +num
	num = num +3
	m = m + 1
print sum,m

total = 0
n = 0
list = []
for x in range(101):
	if x % 4 == 1:
		total = x + total
		n = n + 1
		list.append(x)
print total,n
print len(list)
print list
