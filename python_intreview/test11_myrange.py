#!/usr/bin/env oython3



def myrange(first,second=None,step=1):

  if second is None:
    current = 0
    maxnum = first

  else:
    current = first
    maxnum = second

  if step > 0:
    while current < maxnum:
      yield current
      current += step
  else:
    while current > maxnum:
      yield current
      current += step



#print(list(myrange(8,10)))
print(list(myrange(20,2,-3)))
