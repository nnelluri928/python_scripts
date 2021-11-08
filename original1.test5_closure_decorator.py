#!/usr/bin/env python3




def count_calls(func):
  count = 0
  def call_func(*args,**kwargs):
    nonlocal count 
    count += 1
    print(f"calling {func}, time {count}")
    return func(*args,**kwargs)
  return call_func

@count_calls
def hello(name):
  print(f"Hello , {name}")

hello('world')
hello('world')


#hello = count_call(hello)



