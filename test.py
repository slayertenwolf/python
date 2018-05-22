#!/usr/bin/env python
# coding=utf-8

import copy
wolf =['A','B','C','D',[1,2,3]]
Zombie = copy.copy(wolf)
wolf[1] = 666
print(wolf)
print(Zombie)
x = []
print(type(x))
