#!/usr/bin/python

import os
list = dir(os)
print list
with open('/home/hp/py/test.txt','a') as test:
	for y in list:
		test.write(y+',')
