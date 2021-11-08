#!/usr/bin/env python3


class Person():

  def __init__(self,s):
    self.fullname = s
    self.firstname,self.lastname = s.split()



  @property
  def fullname(self):
    print("\n\nNow executing the fullname method")
    return self.__fullname__
  @fullname.setter
  
  def fullname(self,newname):
    print("\t\tNow executing the fullname setter")

    self.__fullname__ = newname
    self.firstname,self.lastname = newname.split()
















P = Person('Narasimha Nelluri')
print(P.firstname)
print(P.lastname)


P.fullname = 'Harshith Nelluri'

print(P.firstname)
print(P.lastname)
