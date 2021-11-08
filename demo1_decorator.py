#!/usr/bin/env python3


def outer_fn(msg):
  def inner_fn():
    print(msg)
  return inner_fn

hi_fn = outer_fn('Hi')
bye_fn = outer_fn('Bye')

hi_fn()
bye_fn()

