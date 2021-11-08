#!/usr/bin/python3

def mychain(*args):
#!/usr/bin/env python3

s = 'abcde'
list1 = [10,20,30]
t = (100,200,300)

def mychain(*args):

  for one_arg in args:
    for sub_arg in one_arg:
      yield sub_arg


#for one_item in mychain(s,list1,t):
 # print(one_item,end=' ')

print(' '.join(str(one_item) for one_item in mychain(s,list1,t)))
