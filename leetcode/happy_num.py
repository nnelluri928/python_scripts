#!/usr/bin/env python3


def happyNumber(num):

  seen = set()

  while(num):

    cur = num
    val =0
    while(cur):

      last = cur%10
      val += last*2
      cur = cur//10
    if val not in seen:
      seen.add(val)
    else:
      return False
    num = val
    if val ==1:
      return True

print(happyNumber(19))
      
