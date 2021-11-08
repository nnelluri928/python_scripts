#!/usr/bin/env python3

def get_data(aTuple):

  nums = ()
  words = ()
  
  for t in aTuple:
    nums = nums + (t[0],)
    if t[1] not in words:
      words = words + (t[1],)
  
  min_n = min(nums)
  max_n = max(nums)
  
  unique_words = len(words)

  return (min_n, max_n, unique_words)  

overlaps = get_data( [(1,10),(15,20),(101,110)] )
print( "Overlap 1 =", overlaps )

