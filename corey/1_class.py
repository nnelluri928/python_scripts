#!/usr/bin/env python3

class Employee:

  raise_amount = 1.04
  def __init__(self,first,last,salary):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@company.com'
    self.salary = salary


  def fullname(self):
    return '{} {}'.format(self.first,self.last)

  def apply_raise(self):
    self.salary = int(self.salary * self.raise_amount)


emp1 = Employee('corey','scharaf',50000)
emp2 = Employee('test','user',50000)



class Developer(Employee):
  pass

dev1 = Developer('narasimha','nelluri',147000)

print(help(Developer))

