#!/usr/bin/env python3
# -*- coding: utf-8 -*-

score = 'B'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B')
    case 'C':
        print('score is C')
    case _: #表示匹配其他任何情况
        print('score is ???.')

#复杂匹配
age =15
match age:
    case x if x < 10: #表示当age < 10成立时匹配，且赋值给变量x
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11|12|13|14|15|16|17|18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

#匹配列表
args=['gcc','hello.c','world.c']
#args=['clean']
#args=['gcc']

match args:
    #如果仅出现gcc，报错
    case ['gcc']:
        print('gcc: missing source file(s).')
    #出现了gcc，至少指定一个文件
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ',' + ','.join(files))
    #仅出现clean
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')