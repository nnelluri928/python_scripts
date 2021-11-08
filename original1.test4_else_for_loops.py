#!/usr/bin/env python3



s = "abcde"


look_for = "d"


for one_letter in s:

  if one_letter == look_for:
    print(f"Yay! Found {one_letter}")
    break

else:

  print(f"Did *Not* find {look_for}")

