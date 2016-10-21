#!/usr/bin/python
import os
import glob
print os.getcwd()
print os.chdir('..')
print os.chdir('/home/hp/py')
print os.listdir('./')
print glob.glob('*.py')
