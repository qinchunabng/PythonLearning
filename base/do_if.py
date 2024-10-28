#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age=3
if age>=18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

s=input('birth:')
birth=int(s)
if birth<2000:
    print('2000前')
else:
    print('00后')

height=1.68
weight=60

bmi=weight/(height**2)

print('bmi:', bmi)

if bmi>32:
    print('严重肥胖')
elif bmi>28 and bmi<=32:
    print('肥胖')
elif bmi>25 and bmi<=28:
    print('过重')
elif bmi>18.5 and bmi<=25:
    print('正常')
else:
    print('过轻')
