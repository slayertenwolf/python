#!/usr/bin/python

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%s'%(self.name,self.score)
        print self.get_grade()

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else :
            return 'C'


bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
wolf = Student('Wolf Cui',99)
bart.print_score()
lisa.print_score()
wolf.print_score()
