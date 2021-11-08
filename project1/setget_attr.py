#!/usr/bin/env python3


class Person():
  pass



person = Person()


person_info = {'first': 'corey', 'last':'schafer'}


for key,val in person_info.items():
  setattr(person,key,val)

for key,val in person_info.items():
  print(getattr(person,key))


