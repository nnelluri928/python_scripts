#!/usr/bin/env python

def sockpair(num,list1):

  set1 = set()
  count = 0

  for item in list1:
  
    if item in set1:
      set1.remove(item)
      count +=1
    
    else:
      set1.add(item)


  print(set1) 
  return count


list1 = [10,30,20,20,10,10,30,50,10,20]
num = 9

print(sockpair(num,list1))

  
