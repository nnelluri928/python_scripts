#!/usr/bin/env python3

def large_cont_sum(arr):
  if len(arr) == 0:
        return 0
  
  max_sum = cur_sum = arr[0]
  for num in arr[1:]:
    cur_sum += num
    cur_sum = max(cur_sum, num)
    max_sum = max(max_sum, cur_sum)
  return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1])) 
