from numpy import *
arr=array([[[1,2,3,4],
            [5,6,7,8]],
           [[1,2,3,4],
            [5,6,7,8]],
           [[1,2,3,4],
            [5,6,7,8]]])
print(arr[0,1,3])
s=arr[1:,0:1,0:2]
print(s)
r=arr[0:,0:,2:3]
print(r)
#numpy can also perform ==,!=,>=<= and etc
print(arr==r)
print(arr>r)