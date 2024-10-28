#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d={'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])

d["Adam"]=67
d['Jack']=88

#如果key不存在就会报错
# print(d['Thomas'])

#不存在返回none
print(d.get('Thomas'))
#不存在返回-1
print(d.get('Thomas', -1))

#删除key
d.pop('Bob')
print(d)

#dict的key必须是不可变对象
#list是key，作为key就会报错
key=[1,2,3]
d[key]='a list'
