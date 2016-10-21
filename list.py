#!/usr/bin/env python

list = ['Wolf','Jack','Sun','Jane']
print list
print len(list)
print list[1]
print list[-3]
list.append('Frank')
for x in list:
    print x
list.insert(2,'Cui')
list.append('Tom')
for x in list:
    print x
list.pop()
print len(list)
print list 
sum = 0
for x in range(101):
    if x%2 == 0:
        sum = sum + x
print sum
sum = 0
for x in range(101):
    if x%2 == 1:
        sum = sum + x
print sum
sum = 0
for x in range(101):
    sum = sum + x
print sum
