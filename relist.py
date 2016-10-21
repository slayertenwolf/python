#!/usr/bin/python

num = int(raw_input("Enter a 3 number:"))
if num < 100 or num >999 :
	print "You input a wrong number"
else :
	a = num/100
	b = (num%100)/10
	c = num%10
	print b
	print c*100+b*10+a
	
