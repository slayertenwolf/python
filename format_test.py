#!/usr/bin/env python
# coding=utf-8

class Person:
    def __init__(self,name,age):
        self.name,self.age = name,age
    def __str__(self):
            return 'This guy is {self.name},is {self.age} old.'.format(self=self)


print(str(Person('kzc',18)))
tom = Person('Tom',33)
print(str(tom))
