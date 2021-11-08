#!/usr/bin/env python


def find_happy_number(nums):

  set1 = set()

  for num in nums:
    while (num!=1):
      current = num
      sum = 0
      while (current != 0):
        rem = current%10
        sum += rem*rem
        current = current / 10
      
      if sum in set1:
        return False

      num = sum
      set1.add(sum)
    return True


print(find_happy_number([29,19]))

      

