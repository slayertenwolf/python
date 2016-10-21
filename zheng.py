#!/usr/bin/python
# --*-- coding:utf-8 --*--
#求一个自然数和0之间所有能被3和5整除的自然数的个数和和
num = int(raw_input("Enter a number:"))
sum = 0
len = 0
for x in range(num):
	if x != 0 and (x%3 == 0 or x%5 ==0):
		sum = sum + x
		len = len + 1
		print x
print sum
print len
