#!/usr/bin/python

while True:
	a = raw_input("Enter something:")
	if a == "quit":
		break
	if len(a) < 3:
		continue
	print "Input is long enough."
