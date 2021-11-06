#!/usr/bin/env python3

class Base(object):
  def __init__(self):
    print('Base.__init__')
  

class child1(Base):
  def __init__(self):
    super(Base).__init__(self)
    print('child1.__init__')


class child2(Base):

  def __init__(self):
    super(Base).__init__(self)
    print('child2.__init__')




class child3(child1,child2):
  
  def __init__(self):
    super(Base).__init__(self)
    print('child3.__init__')


obj = child3()
