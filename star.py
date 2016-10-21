#! /usr/bin/python
def star(x):
	m = range(x)
	for a in m:
		print ' '*(x-a),'*'*(2*a-1)
	for a in m:
		print ' '*a,'*'*(2*(x-a)-1)
	
