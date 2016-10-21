#!/usr/bin/python

#Filename:buying_list.py

list = ['apple','mango','carrot','banana']

print 'I have',len(list),'items to purchase.'

print 'These items are:',
for item in list:
	print item,
print '\nI also have to buy rice.'
list.append('rice')
print 'My shopping list is now',list

print 'I will sort my list now'
list.sort()
print 'Sorted shopping list is:',list

print 'The first item I will buy is',list[0]
olditem = list[0]
del list[0]
print 'I bought the',olditem
print 'My shopping list is now',list
