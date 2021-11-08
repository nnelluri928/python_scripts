#!/usr/bin/env python3


import itertools


s = 'abcde'
list1 = [10,20,30]
t = (100,200,300)

for one_item in itertools.chain(s,list1,t):
  print(one_item, end=' ')
