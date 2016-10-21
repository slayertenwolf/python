#!/usr/bin/python

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print '%s:%s'%(self.name,self.score),self.upgrade()
#        print self.upgrade()

    def upgrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'
class Girl(Student):
    pass
Wolf = Student('Wolf Cui',99)
John = Student('John Du',68)
Tom = Student('Tom Green',55)
Wolf.print_score()
John.print_score()
Tom.print_score()
Lucy = Girl('Lucy David',90)
Lucy.print_score()

