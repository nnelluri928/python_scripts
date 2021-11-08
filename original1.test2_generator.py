#!/usr/bin/env python3

def read_n(filename,n):


  f = open(filename)
  while True:
    one_chunk = ''.join(f.readline for i in range(n))
    if one_chunk:
      yield one_chunk
    else:
      break



one_chunk = read_n("/etc/passwd",3)
print(one_chunk)


