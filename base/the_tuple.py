#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#元组定义
#元组特点：定义之后不可改变
classmates=('Michael','Bob','Tracy')
print(classmates)

#元素无法修改
#classmates.append('Adam')
#print(classmates)

#定义只有一个元素的元素，需要用','结尾消除歧义
#可以改变量的指向
classmates=(1,)
print(classmates)

#定义一个“可变”的tuple
t=('a','b',['A','B'])
print(t)
t[2][0]='X'
t[2][1]='Y'
print(t)