#!/usr/bin/python

def func():
	global x

	print "x is",x
	x = 88
	print "x is changed.Now x is",x

x = 100
func()
print "In the end x is",x
