#!/usr/bin/env python3


def tuple_overlap(old_list,overlap = None):

  old_list.sort()
  if overlap is None:
    overlap = [] 
  for fir,sec in zip(old_list,old_list[1:]):
      
    if fir[0]<=sec[0]<=fir[1]: 
      overlap.append(fir)
      overlap.append(sec)
    
  overlap = sorted(overlap)
  return overlap 



overlaps = tuple_overlap( [(1,10),(15,20),(101,110)] )
print( "Overlap 1 =", overlaps )
assert overlaps == [] 

overlaps = tuple_overlap( [(1,20),(15,20),(101,110)])
print( "Overlap 2 =", overlaps )
assert overlaps ==[(1, 20),(15, 20)] 

overlaps = tuple_overlap( [(15,20),(1,10),(1,10),(101,110),(1,10)])
print( "Overlap 3 =", overlaps )
assert overlaps == [(1, 10),(1,10),(1,10)]


