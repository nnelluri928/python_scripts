#!/usr/bin/python 

from collections import Counter
from operator import itemgetter

words = [ 'bar','foobar','foo', 'foo']
word_dict = {}



for item in words:
  if item not in word_dict:
    word_dict[item] = 1
  else:
    word_dict[item] += 1
print(word_dict)

print(sorted(word_dict.items(),key=lambda word:word[1], reverse=True))

#words_list = Counter(words)

#print(words_list)
#print(sorted(words_list.items(),key=itemgetter(1),reverse=True))
