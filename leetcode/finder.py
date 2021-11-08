#!/usr/bin/env python3


def finder(arr1,arr2):
    num = 0
    for n in arr1:
        num += n
    for n in arr2:
        num -=n
    return num
    
print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))

arr1 = [5,5,7,7]
arr2 = [5,7,7]

print(finder(arr1,arr2))
