#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates=['Michael','Bob','Tracy']

print("classmates length:", len(classmates))

print(classmates)

print('classmates[0]=', classmates[0])
#访问倒数第一个元素
print('classmate[-1]=', classmates[-1])

# 追加元素
classmates.append('Adam')

print(classmates)

#指定位置插入元素
classmates.insert(1, 'Jack')
print(classmates)

#删除末尾元素
classmates.pop()
print(classmates)

#修改元素
classmates[1]='Sarah'
print(classmates)