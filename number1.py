#!/usr/bin/python
# -*- coding:UTF-8 -*-

n = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a != b)and (b != c)and (a != c):
                print a,b,c
                n = n + 1
print n
m = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if(a == b)or (b == c)or (a == c):
                print a,b,c
                m = m + 1
print m
 
 
