#!/usr/bin/env python
# coding=utf-8

def re_turn(a_list):
    n = 0
    for x in a_list:
        if n < len(a_list) - 1:
            print(x,end=',') 
            n += 1
        else:
            print('and '+ x)

def a_input():
    print('please input a list:')
    a_list = []
    a = input()
    a_list.append(a)
    b = input()
    a_list.append(b)
    c = input()
    a_list.append(c)
    spam = a_list
    return spam
re_turn(a_input())
            
           

