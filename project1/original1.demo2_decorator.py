#!/usr/bin/env phthon3


def decorator_function(original_function):
  

  def wrapper_function():
    print('wrapper is executed this before {}'.format(original_function.__name__)) 
    return original_function()

  return wrapper_function

@decorator_function
def display():
  print("display function is ran")

display()


#decorator_display = decorator_function(display)
#decorator_display()
