#!/usr/bin/env python


def num_coins(cents):
  if cents < 1:
    return 0
  coins = [25,10,5,1]
  num_coins = 0
  for coin in coins:
    num_coins += cents / coin
    print(num_coins)
    cents = cents % coin
    print(cents)
    if cents == 0:
     break
  return num_coins



print(num_coins(31))
