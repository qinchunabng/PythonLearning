#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'ABC'.encode('ascii')

'中文'.encode('utf-8')

len('中文')

print('%2d-%02d' % (3,1))
print('Age: %s. Gender: %s' % (25, True))

print('Hello, {0}, 成绩提升了{1:.1f}%'.format('小明', 17.125))

r=2.5
s=3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')