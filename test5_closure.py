#!/usr/bin/env python3

''' LEGB  -- Identifier look up rule for python
    local
    enclosing function
    global
    builtins

'''



def foo(x):

  def bar(y):
    print(f"I am in bar , x = {x} and y = {y}")
  return bar



b1 = foo(10)
b2 = foo(20)


b1(3)
b2(4)
