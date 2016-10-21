#! /usr/bin/python

def mi(x,y):
	m = 1
	while (y > 0):
		m = m * x
		y = y - 1
	return m

def mi2(a,b):
	z = 1
	i = 1
	while (i <= b):
		z = z * a
		i = i + 1
	return z
