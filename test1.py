#!/usr/binpython3




def highest_score_under(max_num):
  if max_num <= 0:
    return 0
  highest_num = 0
  for num in range(max_num):
    sqare = num ** 2
    if sqare >= max_num:
      break
    highest_num = sqare
  return num,highest_num



print(highest_score_under(1))


