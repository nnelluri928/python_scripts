#!/usr/bin/env python3


def fib(n):

  first = 0
  second = 1
  
  while True:

    yield first
    
    first,second = second , first + second




fib(10)


