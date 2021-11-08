#!/usr/bin/env python3

def sort_by_last_letter(strings):
  def last_letter(s):
    return s[-1]
  return sorted(strings, key = last_letter)



print(sort_by_last_letter(['ghi','def','abc']))

