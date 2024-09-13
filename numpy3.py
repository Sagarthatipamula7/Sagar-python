from numpy import *
arr1=array([1,2,3,4])
arr2=array([[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]])
#the replication takes place here the arr1 becomes like above array
arr3=array([[1,2,3,4],
            [1,2,3,4],
            [1,2,3,4],
            [1,2,3,4]])
print(arr1+arr2)
print(arr2+arr3)
print(arr2 @ arr3)#@indicates multiplication
print(arr1*arr2)