#!/usr/bin/python

def func(x):
	print "x is",x
	x = 78
	print "x is changed. now x is",x

x = 100
func(x)
print "x is still",x
