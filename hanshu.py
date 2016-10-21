#!/usr/bin/python

def sayhello():
	print "hello,world!"

def star(i):
	for x in range(i+1):
		print x*"*"
sayhello()
num = int(raw_input("Enter a number:"))
star(num)
