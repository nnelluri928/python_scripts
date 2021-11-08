
#!/usr/bin/env python3

def Binarysearch(arr,length,x,searchFirst):
    start = 0
    end = length-1
    result = -1

    while (start<= end):
        mid = (start+end)//2
        if x== arr[mid]:
          result=mid
          if(searchFirst):
            end = mid-1  #search towards left (lower index)
          else:
            start  = mid+1 #search towards right (highr index)

        elif x < arr[mid]:
          end = mid-1
        else:
          start = mid +1
    return result


if __name__ == "__main__":
  arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42]
  target = 44
  length = len(arr)
  firstIndex = Binarysearch(arr,length,target,searchFirst=True)
  lastIndex = Binarysearch(arr,length,target,searchFirst=False)

  if firstIndex == -1:
    print("count of {} is zero".format(target))
  else:
    print("count os {} is {}".format(target,lastIndex-firstIndex+1))


